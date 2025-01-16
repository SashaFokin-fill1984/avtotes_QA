import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a19106987ef9c5a98803bf82bb49bb8f'
HEADER = {'cONTENT-tYPE' : 'application/json' , 'trainer_token' : TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "Fill19842605@yandex.ru",
    "password": "Egor2605!@"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_rename = {
    "pokemon_id": "19661",
    "name": "пикака",
    "photo_id": 2
 }


body_pokeball = {
    "pokemon_id": "19554"
}

'''response = requests.post(url= f'{URL}/trainers/reg', headers=HEADER, json=body_registration )
print(response.text)'''

'''response_confirmation = requests.post(url= f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirmation )
print(response_confirmation.text) '''
  
response_create = requests.post(url= f'{URL}/pokemons', headers=HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

response_rename = requests.put(url= f'{URL}/pokemons', headers=HEADER, json = body_rename)
print (response_rename.text)
 
response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_pokeball) 
print(response_pokeball.text)
