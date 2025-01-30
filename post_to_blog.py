import requests; import json; import os
from get_blog_id import f as get_blog_id
from get_datas_to_post import f as get_datas_to_post
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv()

# Function to save credentials
def save_credentials(credentials, filename='credentials.json'):
    with open(filename, 'w') as token:
        token.write(credentials.to_json())

# Function to load credentials
def load_credentials(filename='credentials.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as token:
            creds = Credentials.from_authorized_user_info(json.load(token, indent=4))
        return creds
    return None

# Load the client secrets
with open('client_secret.json', 'r') as file:
    client_secrets = json.load(file)

credentials = load_credentials()

# If no valid credentials, run the OAuth flow
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_config(
            client_secrets,
            scopes=['https://www.googleapis.com/auth/blogger']
        )
        credentials = flow.run_local_server(port=0)
        # Save the credentials for future use
        save_credentials(credentials)

# Get credentials and create a session
credentials = flow.run_local_server(port=0)

session = requests.Session()
session.headers.update({'Authorization': f'Bearer {credentials.token}'})

blog_id = get_blog_id()
api_key = os.getenv('BLOGGER_API_KEY')

endpoint = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts'

headers = {
    'Content-Type': 'application/json'
}

a = get_datas_to_post()
b = a.split('\n')
first_line = True
title = ''
content = ''
for c in b:
    if c != '' and first_line:
        first_line = False
        title = c
    else:
        content += c

# Dados da postagem
post_data = {
    "kind": "blogger#post",
    "blog": {
        "id": blog_id
    },
    "title": title,
    "content": content,
    "status": "LIVE"
}

# Fazer a requisição POST
response = session.post(endpoint, json=post_data)

# Verificar o status da resposta e exibir o conteúdo
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f'Erro na requisição: {response.status_code}')
    print(response.text)
