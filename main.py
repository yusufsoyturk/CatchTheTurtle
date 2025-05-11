import turtle

game_screen = turtle.Screen()
game_screen.title("Catch The Turtle")
game_screen.bgcolor("CadetBlue1")

t_score = turtle.Turtle()
t_time = turtle.Turtle()
t_score.hideturtle()
t_time.hideturtle()

click = 0
game_time = 15

def counter_click(x, y):
    global click
    click += 1
    print(f"{x}, {y}")
    write_score()

def counter_time():
    global game_time
    game_time -= 1
    write_time()

def write_score():
    t_score.clear()
    t_score.penup()
    t_score.goto(0, 300)
    t_score.pendown()
    t_score.write(f"Score: {click}", align="center", font=("Courier", 16, "bold"))

def write_time():
    t_time.clear()
    t_time.penup()
    t_time.goto(0, 270)
    t_time.pendown()
    if game_time > 0:
        game_screen.ontimer(fun=counter_time, t=1000)
        t_time.write(f"Time: {game_time}", align="center", font=("Courier", 16, "bold"))
    else:
        t_time.write("Game Over!" , align="center", font=("Courier", 16, "bold"))

def fun1(x, y):
    print(f"Tıklanan konum: x={x}, y={y}")

write_score()
write_time()
game_screen.listen()
game_screen.onclick(fun=counter_click, btn=1)

turtle.mainloop()

