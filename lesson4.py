# clothes = ['shorts', 'shoes', 't-shirt', ]
# if clothes[0] == 'shorts':
#     clothes[0] = 'warm coat'
# print(clothes)
#
# game_scores = [200, 10, 3, 5, 199, 30, 99, 100, 7, 22]
#
# print(max(game_scores))
# print(min(game_scores))
# print(max(game_scores))
# print(sorted(game_scores))
# print(list(reversed(sorted(game_scores))))

# shopping_list = ['milk', 'coffee', 'cereal', 'bread']
#
# if 'bread' in shopping_list and 'butter' not in shopping_list:
#     shopping_list.append('butter')
#
# print(shopping_list)


# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
# for cost in costs:
#   total_cost = total_cost + cost
# print(total_cost)
#
# print(total_cost/len(costs))

# place = {
# 'name': 'The Anchor',
# 'post_code': 'E14 6HY',
# 'street_number': '54',
# 'location': {
# 'longitude': 127,
# 'latitude': 63,
#     }
# }
#
# print(place['name'],place['post_code'],place['street_number'])
# print(place['location']['latitude'])
# print(place['location']['longitude'])

# longitude
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19}
# ]
# for fruit in fruits:
#     print(fruit['name'], fruit['colour'], fruit['price'])

import random
first_names = ["Alex", "Rex", "Barabara", "Ben", "Tyler"]
last_names = ["lewis", "erwin", "chamberlain", "House", "Clausen"]
chosen_name = random.choice(first_names) + ' ' + random.choice(last_names)
print(chosen_name)