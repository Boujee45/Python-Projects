import turtle

#Create a screen (background)

screen = turtle.Screen()
screen.bgcolor("lightblue") # background color
screen.title("My First Turtle Program")

#Create the turtle

t = turtle.Turtle() # initiate turtle module

'''t.shape("turtle") #shape can be "turtle", "arrow" , "circle" e.t.c
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("arrow")'''

#t.shapesize(10) #shape size on the screen

t.color("green") #color

t.speed(2) #speed 1(slow) to 10(fast)

#Turtle Movements

t.forward(100) # Move forward 100 units
t.backward(50) # Move backward 50 units
t.right(90)    # Move right 90 degrees
t.left(45)     # Move left 45 degrees


#Drawing Shapes

#Square
for _ in range(4):
    t.forward(100)
    t.right(90)

#Circle

t.circle(50) #radius 50

#Triangle

for _ in range(3):
    t.forward(100)
    t.left(120)

#Pen Control
'''
t.penup() #lift pen (no drawing)
t.goto(-100, 100) #move to position
t.pendown() #put pen down (drawing starts)

t.pensize(3) # Set pen thickness
t.pencolor("red") #Set pen thickness'''

#Filling Colors

t.begin_fill()
t.color("yellow")

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill() #Fills the square yellow

#Writing Text

t.color("white")
t.write("LOVE", font=("Arial", 32, "bold"))

screen.mainloop() #maintain the screen (readline)

turtle.done() #closing the window
