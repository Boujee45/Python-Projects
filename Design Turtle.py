from turtle import *
from colorsys import *

tracer(50)
bgcolor('black')
pensize(3)
h = 0

goto(100, -300)

for i in range(60):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.01
    for j in range(2):
        circle(140, 90)
        left(180)
        circle(80, 90)
        left(80)

    right(89)
done()
