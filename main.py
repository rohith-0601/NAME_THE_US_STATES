from turtle import Turtle,Screen
import pandas
#temporary variables
state_count = 0
minutes = 10
seconds = 0
game_on = True


# screen settings
screen = Screen()
screen.screensize(721,491)
screen.title("NAME THE US STATES")
screen.bgcolor("black")
screen.bgpic("blank_states_img.gif")

# calling the data
data = pandas.read_csv("50_states.csv")

#creating a timer
timer = Turtle()
timer.hideturtle()
timer.penup()
timer.pencolor("white")
timer.goto(700,480)
def timer_on_screen():
    global minutes,seconds,game_on

    time_display = f"{minutes:02}:{seconds:02}"

    timer.clear()
    screen.title(f"NAME THE STATES :{time_display}")

    if minutes == 0 and seconds == 0:
        timer.clear()
        timer.write("TIME'S UP!",align ="center",font=("Arial", 48, "bold"))
        game_on = False
    elif seconds == 0:
        minutes -= 1
        seconds = 59
    else:
        seconds -= 1
    if game_on:
        screen.ontimer(timer_on_screen,1000)


#let's start game
guess_input = []
while game_on:
    #starting the timer
    timer_on_screen()
    user_input = screen.textinput("ENTER THE STATE NAME",f"{state_count}/50")
    if user_input.lower() in data["state"].str.lower().values:
        if user_input.lower() not in guess_input:
            state_count += 1
            guess_input.append(user_input.lower())

            #find the coordinates
            the_row = data[data["state"].str.lower() == user_input.lower()]
            x_coord = the_row["x"].iloc[0]
            y_coord = the_row["y"].iloc[0]

            #pen to write name
            pen = Turtle()
            pen.hideturtle()
            pen.pencolor("black")
            pen.penup()
            pen.pensize(2)
            pen.goto(x_coord,y_coord)
            pen.write(f"{user_input}",align = "center",font=('Arial', 12, 'normal'))

    if game_on and state_count == 50:
        game_on = False
        win = Turtle()
        win.penup()
        win.pensize(2)
        win.color("black")
        win.write("YAY! YOU WON",align= "center",font = ('Arial', 25, 'normal'))

    if state_count == 50:
        game_on = False



screen.exitonclick()