import requests
from pprint import pprint
from collections import OrderedDict
import json


def ingredient():
    ingredient_choice = input("What ingredient would you like to use?\n")
    url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={}'.format(ingredient_choice)
    response = requests.get(url)
    # print(response)
    recipe = response.json()
    cocktails = recipe['drinks']
    for cocktail in cocktails:
        drinks = cocktail["strDrink"]
        print(drinks)

my_cocktails = {}
def choice():
    cocktail_choice = input("Which cocktail would you like to make?\n")
    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={}'.format(cocktail_choice)
    response = requests.get(url)
    # print(response)
    recipe = response.json()
    cocktails = recipe['drinks']
    ingredients = []
    for cocktail in cocktails:
        instructions = cocktail["strInstructions"]
        ingredients.append(cocktail["strIngredient1"])
        ingredients.append(cocktail["strIngredient2"])
        ingredients.append(cocktail["strIngredient3"])
        ingredients.append(cocktail["strIngredient4"])
        ingredients.append(cocktail["strIngredient5"])
        ingredients.append(cocktail["strIngredient6"])
        ingredients.append(cocktail["strIngredient7"])
        ingredients.append(cocktail["strIngredient8"])
        ingredients.append(cocktail["strIngredient9"])
        ingredients.append(cocktail["strIngredient10"])
        ingredients_list = list(filter(None, ingredients))
        glass = cocktail["strGlass"]
    my_cocktails.update({"name": cocktail_choice})
    my_cocktails.update({"ingredients": ingredients_list})
    my_cocktails.update({"glass": glass})
    my_cocktails.update({"instructions": instructions})
    for x, y in my_cocktails.items():
        print(x, y)

def writer():
    add_drink = input("would you like to add the cocktail recipe(s) to a file y/n?\n")
    if add_drink.lower().startswith("y"):
        with open('cocktail.txt', 'w+') as text_file:
            text_file.write(str(my_cocktails))

        with open('cocktail.txt', 'r') as text_file:
            contents = text_file.read()
        pprint(contents)
    elif add_drink.lower().startswith("n"):
        print("No problem, cocktail recipe(s) not added!")
        exit()


ingredient()
choice()
writer()
