import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def draw_spiral(t , length):
    for __ in range(10):
     if length > 5:
        t.forward(length)
        t.right(30)
        draw_spiral(t , length - 5)
draw_spiral(t , 100)

screen.mainloop()