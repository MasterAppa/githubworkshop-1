from turtle import Screen, Turtle

screen = Screen()
t = Turtle()

def ola():

    t.pensize(3)
    t.pencolor('yellow')
    t.circle(20)
    t.pu()
    screen.mainloop()

ola()