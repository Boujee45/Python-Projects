import turtle
import random

turtle.setup(width=800, height=600)
turtle.bgcolor('black')
turtle.tracer(50)
turtle.hideturtle()
turtle.speed(0)

chars = ('010101010101010101010101010101010101010101010'
         '10101010101010101010101010101010101010101010'
         '101010101010101010101010101010101010101010101010101')
num_columns = 40
turtles = []
font = ('Courier', 14, 'normal')

for i in range(num_columns):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color('green')
    x = -380 + i * 20
    y = random.randint(-300,300)
    t.goto(x, y)
    turtles.append(t)

def move_rain():
    for t in turtles:
        char = random.choice(chars)
        t.write(char, align='center', font=font)

        y = t.ycor() - 20
        if y < -300:
            y = 300
            t.goto(t.xcor() + random.randint(-5, 5), y)
            t.color(random.choice(['green', 'lime green', 'forest green']))

        t.goto(t.xcor(), y)

    turtle.update()
    turtle.ontimer(move_rain, 100)

move_rain()
turtle.done()
