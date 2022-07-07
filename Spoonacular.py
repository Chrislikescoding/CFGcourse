import textwrap

import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/extract"

querystring = {"url":"http://www.melskitchencafe.com/the-best-fudgy-brownies/"}

headers = {
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

results = response.json()

print (results)

for count in range(len(results['extendedIngredients'])):
    print(results['extendedIngredients'][count]['original'])

import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

headers = {
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
}

response = requests.request("GET", url, headers=headers)

print(response.text)



url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

headers = {
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
}

response = requests.request("GET", url, headers=headers)


results = response.json()
my_wrap = textwrap.TextWrapper(width = 100)
wrap_list = my_wrap.wrap(text=results['instructions'])
print(response.text)
for line in wrap_list:
   print(line)
