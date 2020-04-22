chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}


price_check = input("enter chocolate item\n")
if price_check in chocolates:
    print(chocolates[price_check])


# import random
# random_ticket = []
# matches = []
#
# lottery_ticket = [11, 23, 56, 77, 34, 39, 68]
# for i in range(7):
#     random_number = random.randint(0, 100)
#     random_ticket.append(random_number)
#     if random_ticket[i] in lottery_ticket:
#         matches.append("yes")
# print(random_ticket)
# print(matches)
# if len(matches) <= 2:
#     print("Sorry, fewer than 3 matches, you are not a winner")
# elif len(matches) == 3:
#     print("you have won £20!")
# elif len(matches) == 4:
#     print("you have won £40!")
# elif len(matches) == 5:
#     print("You have won £100!")
# elif len(matches) == 6:
#     print("you have won £10,000!!")
# else:
#     print("congrats you have won £1,000,000")

import random
random_ticket = []
matches = []
winning = {
    1: "sorry you have fewer than 3 matches",
    2: "sorry you have fewer than 3 matches",
    3: "you've won £20",
    4: "you've won £50",
    5: "you've won £100",
    6: "you've won £10,000",
    7: "you've won £1,000,000",
}
lottery_ticket = [11, 23, 56, 77, 34, 39, 68]
for i in range(7):
    random_number = random.randint(0, 100)
    random_ticket.append(random_number)
    if random_ticket[i] in lottery_ticket:
        matches.append('yes')

print(random_ticket)
print(matches)
if len(matches) in winning:
    print(winning.get(len(matches)))
# if winning[i] == len(matches):
#     print(winning[i])

# if len(matches) <= 2:
#     print(winning[1])
# elif len(matches) == 3:
#     print(winning[3])
# elif len(matches) == 4:
#     print(winning[4])
# elif len(matches) == 5:
#     print(winning[5])
# elif len(matches) == 6:
#     print(winning[6])
# else:
#     print(winning[7])