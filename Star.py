import turtle
import colorsys

'''
screen = turtle.Screen()
t = turtle.Turtle()
screen.title("STAR")

t.begin_fill()
t.fillcolor("blue")
t.speed(2)
for __ in range(36):
    t.forward(500)
    t.right(170)

t.end_fill()

screen.mainloop()'''

#--- Drawing a Star ---
t = turtle.Turtle()
t.color("gold")
t.speed(5)

colors = [colorsys.hsv_to_rgb(i/5, 1, 1) for i in range(5)]

#Draw a star
for i in range(5):
    t.color(colors[i % 5])
    t.forward(200)
    t.right(144) # angle for star

turtle.done()