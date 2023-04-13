import requests

token = 'ea749ee9c45c9eaef5349020fe60c186'


add_pokemons_respons = requests.post('https://pokemonbattle.me:9104/pokemons', 
              headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
                json = ({
      "name": "Буб",
      "photo": "https://dolnikov.ru/pokemons/albums/001.png"}))
print(add_pokemons_respons.text)



change_pokemons_name = requests.put('https://pokemonbattle.me:9104/pokemons', 
              headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
                json = ({
    "pokemon_id": "9161",
    "name": "bub",}))

print(change_pokemons_name.text)



catch_in_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
              headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
                json = ({
    "pokemon_id": "9161"}))

print(catch_in_pokeball.text)