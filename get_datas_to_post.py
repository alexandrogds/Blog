from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def f():
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Não use '```', não use as tags 'head' ou 'body'. Defina você mesmo o público alvo. Não use as tags <header> ou <footer>,"},
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Crie uma postagem para meu blog no Blogspot.com. Inclua um título separado do conteúdo, de forma destacada. No conteúdo, utilize HTML estruturado, incluindo tags semânticas como <article> e <section> se aplicável. Por favor, assegure-se de que o texto seja bem formatado e atraente para leitores online."
            }
        ]
        }
    ],
    response_format={
        "type": "text"
    },
    temperature=1,
    max_completion_tokens=16000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response)
    return response.choices[0].message.content
