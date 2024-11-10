import time
import requests
from django.utils import timezone
from clientes.models import Cliente

def consulta_e_atualiza_clientes():
    
    clientes = Cliente.objects.filter(cnpj__isnull=False)

    for cliente in clientes:
        if cliente.regime_fiscal.id == 1:
            cnpj = cliente.cnpj
            url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
            try:
                resp = requests.get(url)
                if resp.status_code == 200:
                    data = resp.json()

                    simples_info = data.get("simples", {})
                    optante_simples = simples_info.get("simples", "Não")
                    
                    cliente.status = "Ativo" if optante_simples == "Sim" else "Inativo"
                    cliente.ultima_atualizacao = timezone.now()

                    cliente.save()
                    print(f"Atualizado Cliente {cliente.id} - CNPJ: {cnpj}")
                else:
                    print(f"Erro ao consultar o CNPJ {cnpj}: Status {resp.status_code}")
            except requests.RequestException as e:
                print(f"Erro ao consultar o CNPJ {cnpj}: {e}")
            time.sleep(21)
        elif cliente.regime_fiscal.id == 4:
            cnpj = cliente.cnpj
            url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
            try:
                resp = requests.get(url)
                if resp.status_code == 200:
                    data = resp.json()

                    mei_info = data.get("simples", {})
                    optante_mei = mei_info.get("mei", "Não")
                    
                    cliente.status = "Ativo" if optante_mei == "Sim" else "Inativo"
                    cliente.ultima_atualizacao = timezone.now()

                    cliente.save()
                    print(f"Atualizado Cliente {cliente.id} - CNPJ: {cnpj}")
                else:
                    print(f"Erro ao consultar o CNPJ {cnpj}: Status {resp.status_code}")
            except requests.RequestException as e:
                print(f"Erro ao consultar o CNPJ {cnpj}: {e}")
            time.sleep(21)
        else:
            pass
        

