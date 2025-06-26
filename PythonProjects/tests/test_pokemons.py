import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f99d67a3c02ea012aadda2e24d9b7cbc'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN} 
TRAINER_ID = '36452'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Slon'
   
@pytest.mark.parametrize('key, value', [('name', 'Slon'), ('trainer_id', TRAINER_ID), ('id', '346360')])  
def test_parametrize(key, value):
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
     assert response_parametrize.json()['data'][0][key] == value
      