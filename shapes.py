import turtle
window = turtle.Screen()
window.bgcolor("white")
turtle_1 = turtle.Turtle()
turtle_1.shape("turtle")
turtle_1.color("red")
turtle_1.begin_fill()
turtle_1.penup()
turtle_1.goto(-300, 100)
turtle_1.pendown()
turtle_1.forward(100)
turtle_1.left(120)
turtle_1.forward(100)
turtle_1.left(120)
turtle_1.forward(100)
turtle_1.left(120)
for i in range(3):
  turtle_1.forward(100)
  turtle_1.left(120)
turtle_1.end_fill()

import turtle
window = turtle.Screen()
window.bgcolor("white")
turtle_2 = turtle.Turtle()
turtle_2.shape("circle")
turtle_2.color("green") 
turtle_2.begin_fill()
turtle_2.penup()
turtle_2.goto(-100, 50)
turtle_2.pendown() 
turtle_2.circle(80)
turtle_2.end_fill()

import turtle
window = turtle.Screen()
window.bgcolor("white")
turtle_3 = turtle.Turtle()
turtle_3.shape("arrow")
turtle_3.color("purple")
turtle_3.begin_fill()
turtle_3.penup()
turtle_3.goto(150,200)
turtle_3.pendown()
turtle_3.penup()
turtle_3.goto(150,200)
turtle_3.pendown()
for i in range(8):
  turtle_3.forward(100)
  turtle_3.right(45)
turtle_3.end_fill()