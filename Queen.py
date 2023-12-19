import turtle as t
import math

width = 100
height = 100
circle = height / 20
SIZEp = 51

if SIZEp % 2 == 0:
    t.fillcolor('orange')
else:
    t.fillcolor('brown')


t.begin_fill()
for i in range(0, 2):
    t.forward(width)
    t.right(90)
    t.forward(height / 4)
    t.right(90)
t.left(90)
t.forward(height)

lenght = ((height/2)**2 + (width/4)**2)**(1/2)
angle = 63.5

t.circle(circle)
t.right(angle + 90)
t.forward(lenght)
t.left(angle * 2)
t.forward(lenght)
t.circle(circle)
t.right(angle * 2)
t.forward(lenght)
t.left(angle * 2)
t.forward(lenght)
t.circle(circle)
t.right(angle + 90)
t.forward(height)
t.end_fill()

t.mainloop()