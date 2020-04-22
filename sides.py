import turtle
sides = int(input('Number of sides: '))
angle = 360 / sides
side_length = 60
for shape in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()