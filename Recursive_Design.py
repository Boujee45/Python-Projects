import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")

colors = ["red", "orange", "green", "yellow", "purple", "blue"]
t.speed(100)

t.goto(-50,0)

for x in range(360):
    t.pencolor(colors[x%6])
    t.pensize(x/180+1)
    t.forward(x+100)
    t.left(200)
turtle.done()
screen.mainloop()
