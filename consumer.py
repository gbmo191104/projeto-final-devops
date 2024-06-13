import requests

public_api_url = 'https://api.publicapis.org/entries'

response = requests.get(public_api_url)
data = response.json()

for entry in data['entries']:
    user_data = {
        'username': entry['API'],
        'email': entry['Link'],
        'age': 0  
    }

    response = requests.post('http://127.0.0.1:5000/add_user', json=user_data)
    if response.status_code == 201:
        print(f"Usuário adicionado: {user_data['username']}")
    else:
        print(f"Falha ao adicionar usuário: {user_data['username']}, Erro: {response.json()}")