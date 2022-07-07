import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
print(response)

print(response.json)
pokemon = response.json()
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])

moves = pokemon['moves']

for move in moves:
    print(move['move']['name'])