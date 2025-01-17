import datetime
import time
import requests
from django.utils import timezone
from clientes.models import Cliente

def consulta_e_atualiza_clientes(user):
    clientes = Cliente.objects.filter(
        cnpj__isnull=False,
        ativo = True,
        escritorio = user.escritorio                    
    )

    for cliente in clientes:
        cnpj = cliente.cnpj
        url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                simples_info = data.get("simples", {})
                
                if simples_info:
                    if cliente.regime_fiscal and cliente.regime_fiscal.id == 1:  # Simples Nacional
                        optante_simples = simples_info.get("simples", "Não")
                        data_exclusao_simples = simples_info.get("data_exclusao_simples")
                        
                        if optante_simples == "Sim" and not data_exclusao_simples:
                            cliente.status = "Regular"
                        else:
                            cliente.status = "Irregular ou Migrou"
                        
                        cliente.data_inclusao = parse_date(simples_info.get("data_opcao_simples"))
                        cliente.data_exclusao = parse_date(data_exclusao_simples)
                    
                    elif cliente.regime_fiscal and cliente.regime_fiscal.id == 2:  # MEI
                        optante_mei = simples_info.get("mei", "Não")
                        data_exclusao_mei = simples_info.get("data_exclusao_mei")
                        
                        if optante_mei == "Sim" and not data_exclusao_mei:
                            cliente.status = "Regular"
                        else:
                            cliente.status = "Irregular"
                        
                        cliente.data_inclusao = parse_date(simples_info.get("data_opcao_mei"))
                        cliente.data_exclusao = parse_date(data_exclusao_mei)

                cliente.ultima_atualizacao = timezone.now()
                cliente.save()
                print(f"Atualizado Cliente {cliente.id} - CNPJ: {cnpj}")
            else:
                print(f"Erro ao consultar o CNPJ {cnpj}: Status {resp.status_code}")
        except requests.Timeout:
            print(f"Timeout ao consultar o CNPJ {cnpj}.")
        except Exception as e:
            print(f"Erro inesperado para o CNPJ {cnpj}: {e}")
        
        # Evitar sobrecarga no servidor com delay de 21 segundos
        time.sleep(21)

def parse_date(date_str):
    if date_str:
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print(f"Erro ao converter data: {date_str}")
    return None
