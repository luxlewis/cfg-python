import requests
from pprint import pprint
from collections import OrderedDict
import json
recipe_data = {}

def ingredient():
    ingredient_choice = input("what ingredient would you like to use?\n")
    allergen_info = input("great, do you have any allergens?\n")
    url = "https://api.edamam.com/search?q={}&excluded={}&app_id=2b695b92&app_key=6e53ca3d6455374b5a56549359e460df".format(ingredient_choice, allergen_info)

    response = requests.get(url)
    recipe = response.json()
    # print(response)
    results = recipe['hits']
    for result in results:
        recipe_options = result['recipe']
        labels = (recipe_options['label'])
        uris = (recipe_options['uri'])
        recipe_data.update({labels:uris})
    pprint(recipe_data)

my_recipe = {}
def recipe():
    recipe_choice = input("which dish would you like to make?\n")

    url = "https://api.edamam.com/search?q={}&app_id=2b695b92&app_key=6e53ca3d6455374b5a56549359e460df".format(recipe_choice)
    response = requests.get(url)
    recipe = response.json()
    # print(response)
    choices = recipe['hits']
    for choice in choices:
        recipe_list = choice['recipe']
        labels = recipe_list['label']
        ingredients = recipe_list['ingredientLines']
        my_recipe.update({labels:ingredients})
    pprint(my_recipe)

def writer():
    add_recipe = input("would you like to add recipe(s) to a file y/n?\n")
    if add_recipe.lower().startswith("y"):
        with open('recipe.txt', 'w+') as text_file:
            text_file.write(str(my_recipe))

        with open('recipe.txt', 'r') as text_file:
            contents = text_file.read()
        pprint(contents)
    elif add_recipe.lower().startswith("n"):
        print("No problem, recipe(s) not added!")
        exit()
ingredient()
recipe()
writer()

