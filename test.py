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


filtered_dict = dict(filter(lambda item: "strIng" in item[0] , names.items()))

for item in filtered_dict.items():
   print(item)

def choice():
    cocktail_choice = input("Which cocktail would you like to make?\n")
    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={}'.format(cocktail_choice)
    response = requests.get(url)
    # print(response)
    recipe = response.json()
    cocktails = recipe['drinks']
    my_cocktails = {}
    ingredients = []
    for cocktail in cocktails:


filtered_names=filter(filterString,names)

for name in filtered_names:
   print(name)