
"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
from random import choice
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def generar_color():
    color = ['black', 'green', 'blue', 'yellow', 'purple', 'orange', 'grey']
    return choice(color)

color_serpiente = generar_color()
color_comida = generar_color()


if color_comida == color_serpiente:
    color_comida = generar_color()

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_serpiente)

    square(food.x, food.y, 9, color_comida)
    update()
    ontimer(move, 100)

def move_food():
    "Move the food one step randomly without leaving the boundaries."
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = directions[randrange(0, 4)] # Selecciona una dirección al azar
    new_food_position = food + move

    if inside(new_food_position):
        food.move(move)
    else:
        # Intenta otra dirección si la nueva posición está fuera de límites
        move_food()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
