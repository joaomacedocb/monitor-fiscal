import requests
from clientes.models import Cliente

def consulta_cnpjs():
    # Obtém uma lista de CNPJs de clientes
    lista_cnpjs = [cliente.cnpj for cliente in Cliente.objects.all() if cliente.cnpj]

    # Faz a consulta para cada CNPJ na API
    for cnpj in lista_cnpjs:
        url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                data = resp.json()

                # Extrai as informações desejadas
                cnpj = data.get("estabelecimento", {}).get("cnpj", "N/A")
                simples_info = data.get("simples", {})
                optante_simples = simples_info.get("simples", "N/A")
                data_inclusao_simples = simples_info.get("data_opcao_simples", "N/A")
                data_exclusao_simples = simples_info.get("data_exclusao_simples", "N/A")

                # Exibe os resultados
                print(f"CNPJ: {cnpj}")
                print(f"Optante pelo Simples: {optante_simples}")
                print(f"Data de Inclusão no Simples: {data_inclusao_simples}")
                print(f"Data de Exclusão do Simples: {data_exclusao_simples}")
                print("-" * 40)
            else:
                print(f"Erro ao consultar o CNPJ {cnpj}: Status {resp.status_code}")
        except requests.RequestException as e:
            print(f"Erro ao consultar o CNPJ {cnpj}: {e}")
