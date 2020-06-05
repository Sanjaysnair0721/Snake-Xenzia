import turtle
import keyboard
import time
import random

score=0
highscore=0

kali = turtle.Screen()
kali.bgcolor("black")
kali.setup(width=600, height=600)
kali.title("Turtle")
pamb = turtle.Turtle()
pamb.speed(1)
pamb.pencolor("green")
pamb.shape("turtle")
pamb.penup()
pamb.goto(0, 100)
pamb.direction = "stop"

def move():
    if pamb.direction == "up":
        y = pamb.ycor() #y coordinate of the turtle
        pamb.sety(y + 20)
    elif pamb.direction == "down":
        y = pamb.ycor() #y coordinate of the turtle
        pamb.sety(y - 20)
    elif pamb.direction == "right":
        x = pamb.xcor() #x coordinate of turtle 
        pamb.setx(x + 20)
    elif pamb.direction == "left":
        x = pamb.xcor() #x coordinate of turtle 
        pamb.setx(x - 20)
        
def goup():
    if pamb.direction !="down":
        pamb.direction ="up"
def godown():
    if pamb.direction !="up":
        pamb.direction ="down"
def goright():
    if pamb.direction !="left":
        pamb.direction ="right"
def goleft():
    if pamb.direction !="right":
        pamb.direction ="left"

kali.listen()
kali.onkey(goup, "w")
kali.onkey(godown, "s")
kali.onkey(goright, "d")
kali.onkey(goleft, "a")

unda=turtle.Turtle()
unda.speed(0)
unda.shape("circle")
unda.color("red")
unda.penup()
unda.shapesize(0.50, 0.50)
unda.goto(0, 0)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.shapesize(0.50, 0.50)
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
vaals=[]
delay=0.1    
while True:
    kali.update()

    if pamb.xcor()>290 or pamb.ycor()>290 or pamb.xcor()<-290 or pamb.ycor()<-290:
        pamb.goto(0,0)
        pamb.direction = "stop"
        for vaal in vaals:
            vaal.goto(1000,1000)
        vaals.clear()
        score=0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 

    if pamb.distance(unda) <20:#snake and food come in contact
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        unda.goto(x, y)
    
        vaal=turtle.Turtle()#body
        vaal.color("green")
        vaal.shape("square")
        vaal.speed(0)
        vaal.penup()
        vaals.append(vaal)
        score+=10
        if score>highscore:
            highscore=score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 
    
    for index in range(len(vaals)-1, 0, -1):#length of snake increasing
        x = vaals[index-1].xcor()
        y = vaals[index-1].ycor()
        vaals[index].goto(x, y)
    if len(vaals)>0:
        a = pamb.xcor()
        b = pamb.ycor()
        vaals[0].goto(a, b)

    move()

    for vaal in vaals:#collision with body
        if pamb.distance(vaal) <20:
            pamb.goto(0,0)
            pamb.direction = "stop"
            for vaal in vaals:
                vaal.goto(1000,1000)
            vaals.clear()    
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal")) 

    time.sleep(delay)
kali.mainloop()    
    
    

