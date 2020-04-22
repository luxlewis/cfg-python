# new_todos = input('what is your todo?\n')
#
# with open('todo.txt', 'r') as text_file:
#     todos = text_file.read()
#
# todos = todos + ' ' + new_todos + '\n'
#
# with open('todo.txt', 'w+') as text_file:
#     text_file.write(new_todos)
# print(todos)


import csv


with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

print(heights)
shortest_height = min(heights)
print(shortest_height)




