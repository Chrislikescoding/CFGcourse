from typing import List, Any

import requests
from pprint import pprint
#ingredient = 'chicken'
# url = f'https://api.edamam.com/search?q={ingredient}&health={vegan}&app_id={app_id}&app_key={app_key}'

def recipe_search():
    ingredient = input('Enter an ingredient: ')

    health_label = input('What are your dietary requirements? ')

    app_id ='a69d7df8'
    app_key = 'b88a2dd166443ec83973da61cf5dec14'

    response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}&health={health_label}'
                          )


    #response = requests.get(url)
    edamam = response.json()
    print(edamam)
    return edamam['hits']


data_label = []
data_uri = []
data_calories = []

results = recipe_search()


for result in results:

       recipe = result['recipe']
       print(recipe['label'])

     #  print(recipe['ingredients'])
       data_label.append(recipe['label'])
       data_calories.append(recipe['calories'])
       data = {'Label': data_label,
               '': data_calories
                }









