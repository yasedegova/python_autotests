import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f99d67a3c02ea012aadda2e24d9b7cbc'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN} 
body_create = {
    "name": "Slon",
    "photo_id": 12
}
response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)