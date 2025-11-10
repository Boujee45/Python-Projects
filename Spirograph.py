import turtle
import colorsys

'''
screen = turtle.Screen()
t = turtle.Turtle()
screen.title("SPIROGRAPH")
screen.bgcolor("white")
#t.begin_fill()
#t.fillcolor("green")
#t.color("black")

t.speed(20)

colors = [colorsys.hsv_to_rgb(i/36, 1, 1) for i in range(36)]
for i in range(100):
    t.color(colors[i % 36])
    t.circle(60)
    t.right(30)
#t.end_fill()


screen.mainloop()
'''

#--- Colorful Spiral ---

t = turtle.Turtle()
t.speed(0) #fastest speed
turtle.bgcolor("black")

#Colors setup

colors = [colorsys.hsv_to_rgb(i/36, 1, 1) for i in range(36)]
for i in range(80):
    t.color(colors[i % 36])
    t.circle(i * 3)
    #t.forward(i * 2)
    t.right(59)

turtle.done()


