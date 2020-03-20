# 2020 Quarantine python project
# A simple terminal pong game
# By @AbrahamChalave

import turtle

ventana = turtle.Screen()
ventana.title("Pong by @AbrahamChalave")
ventana.bgcolor("black")
ventana.setup(width = 800, height = 600)
ventana.tracer(0)

# Paddles and Ball
# Creating instances and positioning

# P. Left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
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
paddle_b.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(350, 0)

# Ball
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# No resizing, it's fine to keep de square for the ball shape
paddle_a.penup()
paddle_a.goto(0, 0)

#main loop
while true:
    ventana.update()


#video 00:04:22
