import math
import time
from turtle import *

def heart_x(t):
    return 15 * math.sin(t) ** 3

def heart_y(t):
    return 12 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

speed(0)                 
bgcolor("black")
color("#831118")        
hideturtle()

time.sleep(2)           

penup()
goto(0, 0)
pendown()

for i in range(1000):
    t = i / 50           # smooth curve
    x = heart_x(t) * 20
    y = heart_y(t) * 20
    goto(x, y)           # draw out to the heart
    goto(0, 0)           # snap back to center

done()
