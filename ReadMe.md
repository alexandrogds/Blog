# My Blog BlogSpot
O código desse projeto foi feito para gerar posts com a OpenAi e publicar 
em um blog do BlogSpot.

Caso queira publicar em mais de um blog, faça duplicações dessa pasta.

Acesse o console.cloud.google.com, ative a api Bloggger, 
ative o OAuth para pegar o client_secret, diga na configuração do
OAuth que o app é Desktop. Copie o .env.example para .env
e o preencha. Pegue também em console.cloud.google.com uma chave de API.
Faça uma conta na openai e gere uma api key e a coloque no .env.
Instale python.
Copie o json baixado depois de configurar o OAuth renomeie para 
client_secret.json e coloque na mesma pasta desse projeto.

```
pip install -r requirements.txt
```
