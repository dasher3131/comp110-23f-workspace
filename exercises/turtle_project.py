"""EX05: Tree, Sun, Flower Scene!"""

__author__ = "730656282"

from turtle import Turtle, done, tracer, update


def main() -> None:
    """Function to call other functions."""
    turtle_scene = Turtle()
    tracer(0, 0)
    sun(turtle_scene, -300, 250)
    for i in range(-500, 300, 150):
        tree(turtle_scene, i, -200)
        grass(turtle_scene, i, -250)
        flower(turtle_scene, i + 50, -235)  
    update()
    done()


# Creating a function to draw multiple trees in the scene.
def tree(tree: Turtle, x: float, y: float) -> None:
    """Function to draw trees."""
    tree.speed(10)
    tree.hideturtle()
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.color("brown")
    tree.left(90)
    tree.begin_fill()
    tree.forward(20)
    tree.left(90)
    tree.forward(40)
    tree.left(90)
    tree.forward(20)
    tree.left(90)
    tree.forward(40)
    tree.end_fill()
    tree.color("green")
    tree.penup()
    tree.left(90)
    tree.forward(20)
    tree.begin_fill()
    tree.goto(x - 30, y + 70)
    tree.goto(x + 30, y + 70)
    tree.goto(x, y)
    tree.end_fill()


# Creating a function to draw and fill a sun in the scene.
def sun(sun: Turtle, x: float, y: float) -> None:
    """Function to draw the sun."""
    sun.speed(10)
    sun.hideturtle()
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    for _ in range(12):
        sun.forward(30)
        sun.left(150)
    sun.end_fill()


# Creating a function to draw grass on the scene.
def grass(grass: Turtle, x: float, y: float) -> None:
    """Function to draw grass."""
    grass.speed(10)
    grass.hideturtle()
    grass.penup()
    grass.goto(x, y)
    grass.pendown()
    grass.color("green")
    grass.setheading(90)
    grass.width(2)
    for _ in range(50):
        grass.forward(10)
        grass.right(90)
        grass.forward(5)
        grass.right(90)
        grass.forward(10)
        grass.left(90)
        grass.forward(5)
        grass.left(90)
    grass.setheading(0)


# Creating function to draw multiple flowers on the scene.
def flower(flower: Turtle, x: float, y: float) -> None:
    """Function to draw flowers."""
    flower.speed(10)
    flower.hideturtle()
    flower.penup()
    flower.goto(x, y)
    flower.pendown()
    flower.color("green")
    flower.setheading(90)
    flower.width(3)
    flower.forward(40)
    flower.color("red")
    flower.begin_fill()
    for _ in range(8):
        flower.forward(10)
        flower.left(45)
    flower.end_fill()
    flower.color("yellow")
    flower.penup()
    flower.goto(x, y + 10)
    flower.pendown()
    flower.begin_fill()
    flower.circle(5)
    flower.end_fill()


if __name__ == "__main__":
    main()