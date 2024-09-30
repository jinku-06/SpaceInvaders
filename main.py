import turtle
from player import Player
from invader import Invader
from bullet import Bullet
import math
import random

window = turtle.Screen()
window.setup(width=900, height=800)
window.bgcolor("black")
window.title("Space Invader")
window.bgpic("Gifs/space.gif")


# create player, invader
player = Player()
bullet = Bullet()

# Variables
player_speed = 20
bullet_speed = 20
bullet.state = "ready"
number_of_enemies = 5
score = 0

score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(-350, 350)
score_text = f"Score: {score}"
score_pen.write(score_text, False, align="left", font=("Arial", 14))
score_pen.hideturtle()


def move_left():
    player.move_left(player_speed)


def move_right():
    player.move_right(player_speed)


def fire_bullet():
    if bullet.state == "ready":
        x = player.xcor()
        y = player.ycor() + 10
        bullet.fire(x, y)


def isCollision(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    return distance < 15


# Key Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

enemies = []

for _ in range(number_of_enemies):
    enemy = Invader()
    enemies.append(enemy)

# Game Loop
game_over = False
while not game_over:
    window.update()

    # Check if any invader touches the side
    change_direction = False
    for enemy in enemies:
        enemy.move_enemy()
        if enemy.xcor() > 380 or enemy.xcor() < -380:
            change_direction = True

    if change_direction:
        for enemy in enemies:
            enemy.change_direction()

    for enemy in enemies:
        # check collision between the bullet and enemy
        if bullet.state == "fire" and isCollision(bullet, enemy):
            bullet.reset()
            enemy.reset()
            score += 5
            score_text = f"Score: {score}"
            score_pen.clear()
            score_pen.write(score_text, False, align="left", font=("Arial", 14))
            # print("Enemy hit!")

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            game_over = True
            break

    if bullet.state == "fire":
        bullet.move(bullet_speed)

    # Check if bullet is out of bounds
    if bullet.ycor() > 275:
        bullet.reset()

window.bye()
