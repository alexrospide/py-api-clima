# py-api-clima

Script desenvolvido em Python para consumir as informações de clima disponibilizadas pela CPTEC na Brasil API  (https://brasilapi.com.br/)

# :hammer: Funcionalidades do Projeto

- `Argumento Opcional > -c, --cidade`: Nome da cidade que deseja buscar as informações, utilizar aspas para nomes compostos. Caso este parâmetro não for informado, será solicitado via prompt para o usuário.
- `Argumento Opcional > -a, --arquivo`: Informar o nome do arquivo que deseja salvar as informações do clima, caso não informado as informações serão apenas exibidas no terminal
- `Função`: Após receber os parâmetros o script irá buscar o nome da cidade no endpoint /api/cptec/v1/cidade/{nome_cidade} para obter o código da cidade, com o código da cidade será realizada a busca da previsão meteorológica no endpoint /api/cptec/v1/clima/previsao/{código_cidade} e então as informações serão exibidas no terminal. Caso o parâmetro -a, --arquivo nome_arquivo seja recepcionado o script irá armazenar a previsão em um arquivo txt.


# :heavy_check_mark: Tecnologias e Dependências
* Python 3.12
* requests
* click

# :mechanical_arm: Como executar
* Python 3.12 installed required
* Download arquivos do repositório
* Abra o terminal e acesse a pasta do projeto
* python .\previsao_tempo.py --nome_cidade "nome cidade" --arquivo nome_arquivo
  * caso o arquivo já exista, as informações serão adicionadas ao final do arquivo. 
* para mais informações utilize os argumentos -h ou --help 
  * python .\previsao_tempo.py --help 

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=dEV&message=PYTHON&color=GREEN&style=for-the-badge)