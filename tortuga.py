# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Make background
window = turtle.Screen()
window.bgcolor("yellow")

# Make Turtle
creature = turtle.Turtle()
creature.shape("turtle")
creature.shapesize(2, 2, 5)
creature.speed('fastest')

# Hide Turtle
creature.ht()

def draw(side_width, num_sides, pivot_angle, shape_type, stem):
    num_shapes = 360/pivot_angle
    shape_angle = 360/num_sides
    for i in range (0, num_shapes):
        creature.left(pivot_angle)
        if shape_type == "rhombus":
            draw_rhombus(side_width, shape_angle)
        if shape_type == "equilateral":
            for i in range (0, num_sides):
                creature.forward(side_width)
                creature.left(shape_angle)
    if stem == "stem on":
        draw_stem(side_width)

def draw_stem(side_width):
    creature.seth(270)
    creature.forward(side_width*6)
    creature.dot(15)

def draw_rhombus(side_width, shape_angle):
    for i in range(0, 2):
        creature.forward(side_width)
        creature.left(shape_angle)
        creature.forward(side_width)
        creature.left(180 - shape_angle)

def place_turtle(x, y):
    creature.penup()
    creature.setpos(x, y)
    creature.pendown()

place_turtle(-100, 100)
draw(50, 5, 10, "rhombus", "stem on")
place_turtle(100, 100)
draw(50, 5, 10, "rhombus", "stem on")

# Mouth
creature.seth(90)
creature.circle(100,-180)

# Nose
place_turtle(0, -100)
draw(10, 8, 30, "equilateral", "stem off")

window.exitonclick()
