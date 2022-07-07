import requests
import textwrap
names = []
option = ' '
choice = 'No'

# retrieve recipes from the Edamam API
def list_edamam_recipes():
    ingredient = input('Enter an ingredient: ') # multiple can actually be entered - with or without commas
    results = recipe_search(ingredient)
    names = [] # blank dictionary to populate with the name of the recipe and its specific id
    for result in results:
        recipe = result['recipe'] # to get individual recipe details
        print(recipe['label']   ) # print the recipe name
        # load the recipes into a global array variable
        names.append(recipe['label']) # add the recipe name to an array
    return names # return the list of recipe names

# function to access the edamam API with basic criteria
def recipe_search(ingredient):
    app_id ='a69d7df8'
    app_key = 'b88a2dd166443ec83973da61cf5dec14'
    response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}'
     )
    edamam = response.json()
    return edamam['hits']

# process recipes from the Spoonacular API
def list_spoonacular_recipes():

     ingredient = input('Enter an ingredient: ') # multiple can actually be entered - with or without commas
     results = spoonacular_search(ingredient)
     # load the recipes into a global array variable

     for result in results:
         recipe = result # to get individual recipe details
        # originally used a '- ' here but had to change it as it didnt work for recipes that
         # had '-' in the name like 'Hard-boiled eggs
         names.append(recipe['title'] + '*' + str(recipe['id']))
         print(recipe['title'])

     recipe_title = input("To get the full recipe of any of the recipes above, type the recipe name ")
     print_full_recipe(recipe_title)

     return names #return the names for printing the list

def spoonacular_search(ingredient):
     # use rapid api as it's much easier!
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
    # returns a maximum of 8 ingredients
    # ignorePantry means ignore pantry ingredients such as water,salt,flour
    # 1 means maximise used ingredients 2 means minimise missing ingredients
    querystring = {"ingredients": ingredient, "number": "8", "ignorePantry": "true", "ranking": "1"}

    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    spoonacular = response.json()      # this is the data from the API

    return spoonacular                 # send back the data


# function to print ingredients and summary for a chosen recipe
def print_full_recipe(recipe_title):
    # function to search the names list for this title
    recipe_name = ' '
    recipe_name= get_recipe_name(names,recipe_title )
          #search for the '*' to get length of the title
    if (recipe_name != "Not Found"):
        x = recipe_name.find('*')
        recipe_id = recipe_name[x+1:]
         # print the ingredients
        print_ingredients(recipe_id)
        # print the summary
        print_summary(recipe_id)
        #mark the end of the recipe
        print("End of Recipe")
    #check what happens for this API
        choice=input("Would you like to print more analysis for this recipe(Type Yes)?")
        if choice.lower() == 'yes':
            print_recipe_analysis()

#function to get recipe name
def get_recipe_name(names,recipe_title):
    i = index_containing_substring(names, recipe_title)
    if i > -1:
        return names[i]
    else:
        return 'Not Found'

#function to get the index of the names list that contains the name and id we want
def index_containing_substring(names, recipe_title):
    print(recipe_title)
    for i, s in enumerate(names):
        if recipe_title in s:
            return i
    print("This recipe is not in the spoonacular database")
    return -1


def print_ingredients(recipe_id):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + recipe_id + "/ingredientWidget.json"

    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    results = response.json()

    for count in range(len(results['ingredients'])):
        amount = (results['ingredients'][count]['amount']['metric']['value'])
        unit = (results['ingredients'][count]['amount']['metric']['unit'])
        ingredient = (results['ingredients'][count]['name'])
        print(str(amount) + ' ' + unit + ' ' + ingredient)


def print_summary(recipe_id):
     url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + recipe_id + "/information"


     headers = {
    	 "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    	 "X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
      }

     response = requests.request("GET", url, headers=headers)
     results = response.json()

     my_wrap = textwrap.TextWrapper(width = 100)
     wrap_list = my_wrap.wrap(text=results['summary'])

     for line in wrap_list:
         from bs4 import BeautifulSoup
         new_line = BeautifulSoup(line)
         print(new_line.get_text())

def print_recipe_analysis():
    #for count in range(len(results['ingredients'])):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/nutritionWidget.json"

    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
    }
    response = requests.request("GET", url, headers=headers)
    analysis = response.json()
# print selected pieces of information
    print('calories ' + (analysis['calories']))
    print('carbs ' + (analysis['carbs']))
    print('fat ' + (analysis['fat']))
    print('protein ' + (analysis['protein']))

    return analysis

# function to save a single recipe to a file
def save_recipe(recipe):
    with open('cook_book.txt', 'w+') as text_file:
             text_file.write('recipe' + recipe)

#function to write each printed recipe title to your cookbook file
def save_listofrecipes(recipes):
        with open('cook_book.txt', 'w+') as text_file:

            for recipe in recipes:
                 text_file.write(recipe + '\n' )

#function to read and print out your cookbook
def print_listofrecipes():
    with open('cook_book.txt', 'r') as text_file:
        contents = text_file.read()
        print(contents)

def print_options():
    print(' ')
    print('To enter an ingredient and get a list of recipes using Edamam API, type "recipe" ')
    print('To enter an ingredient and get a list of recipes using Spoonacular  API, type "more recipes" ')
    print('To add all of the recipes recently displayed to your CFG cook book type "save list" ')
    print('To add the recipe you just typed in to your CFG cook book type "save" ')
    print('To add your favourite recipe to your CFG cook book type in the name of the recipe to save ' )
    print('To print out your CFG cook book type "print" ')
    option = input("Type here: ")
    return option


def selections():
    run = True
    while run == True:
     option = print_options()
     if (option.lower() == 'recipe'):
      recipes=list_edamam_recipes()
     elif option.lower() == 'more recipes':
        recipes = list_spoonacular_recipes()
     elif option.lower() == 'save list':
        save_listofrecipes(recipes)
     elif option.lower() != '':
        save_recipe(recipe)
     elif option.lower() == 'print':
        print_listofrecipes()
     elif option.lower() == 'quit':
        run=False
     else:
        print("Please enter one of the choices above: 'recipe','more recipes','save','print'  or enter 'quit' to exit")

# starts here:
selections()






