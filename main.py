import turtle
import random
import tkinter.messagebox as msgbox

from turtle import Turtle, Screen

screen = Screen()
screen.setup(550, 220)

def draw_finish():
    finish = Turtle(shape='classic')
    finish.setheading(270)
    finish.penup()
    finish.goto(x=230,y=90)
    finish.pendown()
    finish.goto(x=230, y=-90)

def finish(u_entry,t_dict):
    for color, turtle_object in t_dict.items():
        if turtle_object.xcor() >= 214 and u_entry == color:
            msgbox.showinfo("Race Result", f"Your Color {color} won the race!")
            return turtle_object
        elif turtle_object.xcor() >= 214:
            msgbox.showinfo("Race Result", f"Color {color} won the race!")
            return turtle_object
    else:
        return False

def race():

    # global turtle_dict

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    start_x = -230
    start_y = -60
    turtle_dict = {}
    to_the_races = True

    for i in range (len(colors)):
        t = Turtle(shape='turtle')
        t.penup()
        t.color(colors[i])
        t.goto(x= start_x,y= start_y)
        turtle_dict[colors[i]] = t
        start_y += 20
        t.forward(random.randint(1,3))

    draw_finish()

    while True:
        if finish(user_bet, turtle_dict):  # single call
            break
        for t in turtle_dict.values():
            t.forward(random.randint(1, 5))



def main():
    while True:
        race()
        again = screen.textinput("Go again?", "Would you like to race again?").lower()
        if again in ("y", "yes"):
            screen.clearscreen()
            screen.setup(550, 220)
        if again not in ("y", "yes"):
            break
    screen.exitonclick()



main()
