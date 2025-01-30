import requests; import json; import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

def f():
    # Substitua pelo URL do blog que você deseja buscar
    blog_url = os.getenv('BLOG_URL')

    # Substitua pela sua API Key do Google Blogger
    api_key = os.getenv('BLOGGER_API_KEY')

    # Endpoint da API
    endpoint = 'https://www.googleapis.com/blogger/v3/blogs/byurl'

    # Parâmetros da requisição
    params = {
        'url': blog_url,
        'key': api_key
    }

    # Fazer a requisição GET
    response = requests.get(endpoint, params=params)

    # Verificar o status da resposta e exibir o conteúdo
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data['id'], indent=4))
        return data['id']
    else:
        print(f'Erro na requisição: {response.status_code}')
