import turtle



def triangle(side_length, color):

    angle = 120
    turtle.color(color, color)
    turtle.begin_fill()
    for side in range(3):

        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()

turtle.done

triangle(100, 'pink')