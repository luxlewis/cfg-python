eggs_per_carton = 6
total_cartons = 5
eggs_per_omelette = 4
total_omelettes = (eggs_per_carton * total_cartons) / eggs_per_omelette
output = "you can make {} omelettes with {} cartons of eggs".format(total_omelettes, total_cartons)
print(output)
