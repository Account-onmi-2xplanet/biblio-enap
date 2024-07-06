import requests
import json

def testar(number):
    url = "http://aplicacao-enap2-env.eba-nyajzvk5.us-east-1.elasticbeanstalk.com/api"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"number": number})
    
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    
    print("Resposta recebida do servidor:")
    print(response_json)  # Mostra a resposta JSON recebida da API
    
    # Verificando se 'resposta' está na resposta JSON antes de tentar acessá-la
    if 'resposta' in response_json:
        print(response_json['resposta'])
    else:
        print("Chave 'resposta' não encontrada na resposta JSON.")