import turtle
import random

"Turns off drawing animation"
turtle.tracer(0)

game_screen = turtle.Screen()
game_screen.title("Catch The Turtle")
game_screen.bgcolor("CadetBlue1")

t_score = turtle.Turtle()
t_time = turtle.Turtle()
t_turtle = turtle.Turtle()

t_score.hideturtle()
t_time.hideturtle()
t_turtle.hideturtle()
t_turtle.speed(0)

click = 0
game_time = 30
game_time2 = 30
i = 0
j = 0

def counter_click(x, y):
    global click
    for t in [t_turtle]:
        if t.distance(x, y) < 30:
            click += 1
        print(f"{x}, {y}")
    write_score()

def counter_time():
    global game_time
    game_time -= 1
    write_time()

def counter_time2():
    global game_time2
    game_time2 -= 1
    random_turtle()

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

t_turtle.color("green")
def draw_turtle(a, b):
    t_turtle.penup()
    t_turtle.setheading(0)
    t_turtle.goto(a, b)
    t_turtle.pendown()

    t_turtle.begin_fill()
    t_turtle.right(45)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.left(90)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.end_fill()


    t_turtle.penup()
    t_turtle.goto(a,b)
    t_turtle.pendown()

    t_turtle.begin_fill()
    t_turtle.right(90)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.left(90)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.end_fill()

    t_turtle.penup()
    t_turtle.goto(a,b)
    t_turtle.pendown()

    t_turtle.begin_fill()
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.left(90)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.end_fill()

    t_turtle.penup()
    t_turtle.goto(a,b)
    t_turtle.pendown()

    t_turtle.begin_fill()
    t_turtle.right(90)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.left(90)
    t_turtle.forward(20)
    t_turtle.left(90)
    t_turtle.forward(4)
    t_turtle.end_fill()

    t_turtle.penup()
    t_turtle.goto(a + 8,b + 8)
    t_turtle.pendown()

    t_turtle.begin_fill()
    t_turtle.circle(12)
    t_turtle.end_fill()

    t_turtle.penup()
    t_turtle.goto(a + 16,b + 4)
    t_turtle.pendown()

    t_turtle.begin_fill()
    t_turtle.circle(4)
    t_turtle.end_fill()

def draw_turtle2():
    global i, j
    i = random.randint(-280, 280)
    j = i

    draw_turtle(i, j)

def random_turtle():
    t_turtle.clear()
    if game_time > 1:
        game_screen.ontimer(fun=counter_time2, t=3000)
        draw_turtle2()
    print(game_time)


random_turtle()
write_score()
write_time()
game_screen.listen()

game_screen.onclick(fun=counter_click, btn=1)

# Manually update the screen, show the drawing
turtle.update()
turtle.mainloop()