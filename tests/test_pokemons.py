import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a19106987ef9c5a98803bf82bb49bb8f'
HEADER = {'cONTENT-tYPE' : 'application/json' , 'trainer_token' : TOKEN }
TRAINER_ID = '18159' 


def test_status_code():
    response = requests.get(url= f'{URL}/pokemons' , params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    respose_get = requests.get(url= f'{URL}/pokemons' , params = {'trainer_id' : TRAINER_ID})
    assert respose_get.json()["data"][0]["name"] == 'ludicolo'

@pytest.mark.parametrize('key, value', [('name', 'ludicolo'),('trainer_id' , TRAINER_ID),('id', '195482')])
def test_parametrize(key,value):
    respose_parametrize = requests.get(url= f'{URL}/pokemons' , params = {'trainer_id' : TRAINER_ID})
    assert respose_parametrize.json()["data"][0][key] == value