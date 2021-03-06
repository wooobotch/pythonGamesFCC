# 2020 Quarantine python project
# A simple terminal pong game
# By @AbrahamChalave

import turtle
import os #This works for linux and mac, swap comments between this line and the following to make it work for windows
#import.winsond

ventana = turtle.Screen()
ventana.title("Pong by @AbrahamChalave")
ventana.bgcolor("black")
ventana.setup(width = 800, height = 600)
ventana.tracer(0)

# Puntajes
score_a = 0
score_b = 0

# Paddles and Ball
# Creating instances and positioning

# P. Left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
# Since I picked square for the shape
#it's got to be reshaped in order to look more like a paddle
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
# PenUp to finish drawing
paddle_a.penup()
# Set position 350 units (px) to the left
paddle_a.goto(-350, 0)

# P. Right
# Same way I did with the left paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
# No resizing, it's fine to keep de square for the ball shape
bola.penup()
bola.goto(0, 0)
bola.dx = 2
bola.dy = 2

# Scoring
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Red Player: 0 - Blue Player: 0", align = "center", font = ("Courier", 24, "normal"))

# Functions
# moving paddles
def paddle_a_up():
    y = paddle_a.ycor()
    # ycor() is a Turtle method
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Bindings
# In order to call the funtions created we need to read keyboard input
ventana.listen()
ventana.onkeypress(paddle_a_up, "w")
# It listens to lower case w
ventana.onkeypress(paddle_a_down, "s")
# Arrows must be capitalized
ventana.onkeypress(paddle_b_up, "Up")
ventana.onkeypress(paddle_b_down, "Down")

#main loop
while True:
    ventana.delay(500)
    ventana.update()

    # Some moving
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # It's time to prevent things from going out of the window
    # keeping in mind the size of the ball and the distances
    # from the center of the window

    # Top and bottom limits
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        # The (-1) factor reverts the direction of the ball
        os.system("aplay bounce.wav&") #This works for linux, for windows uncomment the following
#        winsound.Playsound("bounce.wav", winsound.SND_ASYNC)
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        os.system("aplay bounce.wav&")

    # Right and Left limits (goals), then goes back to the center
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_a += 1
        marcador.clear()
        marcador.write("Red Player: {} - Blue Player: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_b += 1
        marcador.clear()
        marcador.write("Red Player: {} - Blue Player: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    # Collisions sections
    # Right paddle
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paddle_b.ycor() + 40 and bola.ycor() > paddle_b.ycor() -40):
        bola.setx(340)
        bola.dx *= -1
        os.system("aplay bounce.wav&")
    # Left paddle
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paddle_a.ycor() + 40 and bola.ycor() > paddle_a.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
        os.system("aplay bounce.wav&")


# That's it. The concepts are covered, it doesn't work the same for every computer, so i added delay() calls
