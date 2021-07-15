# import turtle 
# window = turtle.Screen()
# window.bgcolor("black")

# turtle = turtle.Turtle()
# turtle.speed(1)
# turtle.pensize(1)
# turtle.shape("turtle")
# turtle.color("purple")
# turtle.forward(50)
# turtle.left(90)
# turtle.color("orange")
# turtle.forward(100)
# turtle.left(90)
# turtle.color("green")
# turtle.forward(50)
# turtle.left(90)
# turtle.color("blue")
# turtle.forward(100)

import turtle
window = turtle.Screen()
window.setup(500,500)
window.bgcolor("black")
random_turtle = turtle.Turtle()
random_turtle.speed(10)

def drawCircle():
  random_turtle.color("blue")
  random_turtle.forward(100)
  random_turtle.left(90)
  random_turtle.color("violet")
  random_turtle.forward(100)
  random_turtle.left(90)
  random_turtle.color("orange")
  random_turtle.forward(100)
  random_turtle.left(90)
  random_turtle.color("green")
  random_turtle.forward(100)

x = 0
while x < 36:
  drawCircle()
  random_turtle.right(10)
  x += 1

