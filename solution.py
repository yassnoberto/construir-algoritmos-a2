import requests
from datetime import datetime, timedelta

def cotar():
    cotacoes = []
    data = datetime.now()

    for i in range(365):
        dia = data - timedelta(i)

        while True:
            data_formatada = datetime.strftime(dia, "%m-%d-%Y")

            url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'&$top=100&$format=json&$select=cotacaoCompra"

            res = requests.get(url, timeout=10)
            res = res.json()

            if res['value']:
                cotacoes.append(res['value'][0]['cotacaoCompra'])
                break

            dia = dia - timedelta(1)

    return cotacoes

print(cotar())