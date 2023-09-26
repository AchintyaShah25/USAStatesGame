import turtle
import pandas

screen = turtle.Screen()
screen.title("Achintya's US States game")
img = "blank_states_img.gif"
screen.addshape(img)
screen.setup(height=500, width=750)
turtle.shape(img)

states_data = pandas.read_csv("50_states.csv")
li = states_data.state.to_list()
guessed = []

while len(guessed) < 50:
    ans = screen.textinput(title=f"{len(guessed)}/50 Guessed", prompt="Guess the state").title()

    if ans == "Exit":
        missing = [s for s in li if s not in guessed]
        data = pandas.DataFrame(missing)
        data.to_csv("Not_Guessed.csv")
        break

    if ans in li:
        guessed.append(ans)
        tut = turtle.Turtle()
        tut.penup()
        tut.hideturtle()
        st = states_data[states_data.state == ans]
        xcor = (int(st.x))
        ycor = (int(st.y))
        tut.goto(xcor, ycor)
        tut.write(ans)
