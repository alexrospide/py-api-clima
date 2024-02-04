import requests
import click


@click.command()
@click.option('-c', '--nome_cidade', prompt='Digite o nome da cidade: ', help='Digite o nome da cidade')
@click.option('-a', '--arquivo', help='Salva os dados do clima no arquivo desejado')
def obter_previsao_tempo(nome_cidade, arquivo):
    codigo_cidade = ''
    nome_cidade_alterado = nome_cidade.replace(' ', '%20')

    url = f'https://brasilapi.com.br/api/cptec/v1/cidade/{nome_cidade_alterado}'
    resposta = requests.get(url)
    data = resposta.json()

    if resposta.status_code == 200:
        for ct in data:
            if ct["nome"] == nome_cidade:
                codigo_cidade = ct["id"]
    else:
        print(f'Erro ao obter nome da cidade: {resposta.status_code}')
        return

    url = f'https://brasilapi.com.br/api/cptec/v1/clima/previsao/{codigo_cidade}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        exibir_previsao(dados, arquivo)
    else:
        print(f'Erro ao obter previsão do tempo para a cidade {nome_cidade}. Código de status: {resposta.status_code}')


def exibir_previsao(dados, arquivo):
    lista_informacoes = []
    if dados:
        lista_informacoes.append(f'Cidade: {dados["cidade"]} / {dados["estado"]}')
        lista_informacoes.append(f'Atualizado em: {dados["atualizado_em"]}')
        lista_informacoes.append(f'Condição: {dados["clima"][0]["condicao_desc"]}')
        lista_informacoes.append(f'Mínima de: {dados["clima"][0]["min"]} ºC')
        lista_informacoes.append(f'Máxima de: {dados["clima"][0]["max"]} ºC')
        lista_informacoes.append(f'Índice UV: {dados["clima"][0]["indice_uv"]}')
        lista_informacoes.append(f'-----')

    else:
        print('Falha ao obter dados de previsão do tempo.')

    for info in lista_informacoes:
        print(info)

    if arquivo:
        # nome_arquivo = arquivo if arquivo is not None else f'clima_hoje_em.txt'
        nome_arquivo = arquivo
        with open(nome_arquivo + '.txt', 'a+', encoding='utf-8') as arq:
            for i in lista_informacoes:
                arq.write(f'{i}\n')


if __name__ == '__main__':
    obter_previsao_tempo()
