import turtle
t=turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.speed(0)
t.shape('triangle')
t.hideturtle()
def rm(i):
    k=1
    x=20
    while k<i:
        t.pensize(2)
        t.color('green')
        t.circle(1000)
        t.pensize(5)
        t.color('black')       
        t.left(20)
        t.forward(10)
        t.right(15)
        t.backward(20)
        k=k+1
        x=x-20
rm(100)
t.penup()
t.goto(30,30)
t.pendown()
rm(100)
t.penup()
t.goto(-20,100)
t.pendown()
rm(100)
turtle.done()
