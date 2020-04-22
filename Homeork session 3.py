# is_raining = input("is it raining? y/n \n")
# if is_raining == 'y':
#     print("take umbrella")
# else:
#     print("you dont need an umbrella")

book_century = int(input("what are the first 2 numbers of the book year?\n"))

if book_century == 18:
        century = "eighteenth"
else:
    century = "nineteenth"
book_decade = int(input("what are the last 2 numbers of the book year?\n"))

if book_decade <= 59 and book_decade >= 50:
        decade = "fifties"
elif book_decade <= 69 and book_decade >= 60:
        decade = "sixties"
elif book_decade <= 79 and book_decade >= 70:
        decade = "seventies"
elif book_decade <= 89 and book_decade >= 80:
        decade = "eighties"
elif book_decade <= 99 and book_decade >= 90:
        decade = "ninties"
elif book_decade <= 9 and book_decade >= 0:
        decade = "Naugties"
elif book_decade <= 19 and book_decade >= 10:
        decade = "Tens"
elif book_decade<= 29 and book_decade >= 20:
        decade = "Twenties"
elif book_decade <= 39 and book_decade >= 30:
        decade = "thirties"
else:
        decade = "forties"



print("{}, {}".format(century, decade))