import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("House")

t = turtle.Turtle()
t.speed(0)
#t.color("gold")

#Function to draw a square
def draw_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

#Function to draw a triangle
def draw_triangle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

#Function to draw a circle
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

#Draw house base
t.penup()
t.goto(-100, -130)
t.pendown()
draw_square(200, "yellow")

#Draw roof
t.goto(-100, -130)
t.left(90)
#t.forward(200)
t.right(30)
draw_triangle(200, "brown")

#Draw Door
t.penup()
t.goto(-30, -330)
t.pendown()
t.left(60)
t.right(30)
draw_square(60, "blue")

#Draw windows

t.penup()
t.goto(-80, -230)
t.pendown()
draw_square(40, "white")

t.penup()
t.goto(40, -230)
t.pendown()
draw_square(40, "white")

#Draw sun
t.penup()
t.goto(150, 170)
t.pendown()
draw_circle(50 , "orange")

#Draw tree trunk
t.penup()
t.goto(-350, -350)
t.pendown()
draw_square(40, "brown")

t.penup()
t.goto(-350, -310)
t.pendown()
draw_square(40, "brown")

t.penup()
t.goto(-350, -270)
t.pendown()
draw_square(40, "brown")

t.penup()
t.goto(-350, -230)
t.pendown()
draw_square(40, "brown")

t.penup()
t.goto(-350, -209)
t.pendown()
draw_square(40, "brown")

t.penup()
t.goto(-350, -188)
t.pendown()
draw_square(40, "brown")



#Draw tree leaves
t.penup()
t.goto(-270, -90)
t.pendown()
draw_circle(60, "green")

t.penup()
t.goto(-230, -40)
t.pendown()
draw_circle(60, "green")

t.penup()
t.goto(-320, -40)
t.pendown()
draw_circle(60, "green")


t.penup()
t.goto(-270, -10)
t.pendown()
draw_circle(60, "green")

t.penup()
t.goto(-330, -110)
t.pendown()
draw_circle(60, "green")

t.penup()
t.goto(-210, -110)
t.pendown()
draw_circle(60, "green")


#Draw Grass
t.color("green")
for x in range(-710, 700, 20):
    t.penup()
    t.goto(x, -350)
    t.pendown()
    draw_square(20, "green")

turtle.done()
