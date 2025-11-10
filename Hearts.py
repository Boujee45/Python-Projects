import math
import turtle
from turtle import *
import time
import winsound
'''
title("LOVE")

def heart_a(k):
    return 15 * math.sin(k) ** 3
def heart_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(100)
bgcolor("black")


for i in range(100):
    x = heart_a(i) * 20
    y = heart_b(i) * 20
    goto(x, y)
    for j in range(5):
        color("green")
        #fillcolor("green")
        goto(x , 0)

done()
'''

'''
#--- HEART ---

#Setup Screen

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("LOVE")

t = turtle.Turtle()
t.speed(5)


#--- Write LOVE text ---
t.penup()
t.goto(25, -160)
t.pendown()
t.color("white")
t.write("LOVE", font=("Arial", 32, "bold"))



#Draw Heart

t.color("red")
t.begin_fill()
t.penup()
t.goto(-2, -150)
t.pendown()
t.left(50)
t.forward(270)
t.circle(100, 200)
t.right(140)
t.circle(100, 200)
t.forward(270)
t.end_fill()


turtle.done()
'''

# --- BEATING HEART ---

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("HEART BEAT LOVE")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_heart(size, color):
    t.penup()
    t.goto(0, -size/1.5)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(50)
    t.forward(size)
    t.circle(size/2, 200)
    t.right(140)
    t.circle(size/2 , 200)
    t.forward(size)
    t.end_fill()

# Animation loop
for _ in range(20): #number of beats

#while True: #infinite loop
    t.clear()

    #small heart
    draw_heart(200, "red")
    t.penup()
    t.goto(-35, -20)
    t.pendown()
    t.color("white")
    t.write("LOVE", font=("Arial", 28, "bold"))
    winsound.Beep(500, 200) #Low thump sound
    time.sleep(0.3)

    t.clear()

    #Bigger heart
    draw_heart(270, "red")
    t.penup()
    t.goto(-40, -25)
    t.pendown()
    t.color("white")
    t.write("LOVE", font=("Arial", 32, "bold"))
    winsound.Beep(800, 200) #Higher thump sound
    time.sleep(0.3)

turtle.done()