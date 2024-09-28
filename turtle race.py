from turtle import Turtle , Screen
import random
window = Screen()
window.title("Turtle Race")
window.setup(width=600, height=400)
colors=("red","hotpink","purple")
y_positions=(-70,0,70)

turtles =[]
user_bet = window.textinput(title="Make your bet",prompt="guess the winner:\n Type a color:red,hotpink,purple")#global

for i in range (3):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-280,y=y_positions[i])
    turtles.append(new_turtle)

def race_turtles():
    is_race_on=True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor()>280:
                is_race_on= False
                winning_color = turtle.pencolor()
                display_result(winning_color==user_bet) #هباصي المعلومة لانها مش global
            else:
                turtle.forward(random.randint(1,5))

def display_result(is_winner):
    result_turtle=Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0,0)
    result_turtle.pendown()

    if is_winner:
        window.bgcolor("yellow")
        result_turtle.color("white")
        result_turtle.write("you win!" , align="center" ,font=("arial",35,"bold"))
    else:
        window.bgcolor("brown")
        result_turtle.color("white")
        result_turtle.write("you lose" , align="center" ,font=("arial",35,"bold"))
race_turtles()

window.exitonclick()