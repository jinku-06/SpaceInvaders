import turtle
import random


class Invader(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("Gifs/invader.gif")
        self.shape("Gifs/invader.gif")
        self.penup()
        self.speed(0)
        self.setposition(random.randint(-350, 300), random.randint(200, 300))
        self.enemy_speed = 2
        self.move_down_distance = 40

    def move_enemy(self):
        x = self.xcor()
        x += self.enemy_speed
        self.setx(x)

    def change_direction(self):
        """Moves down all the enemies when they touch side"""
        self.enemy_speed *= -1
        y = self.ycor()
        y -= self.move_down_distance
        self.sety(y)

    def reset(self):
        self.setposition(random.randint(-350, 300), random.randint(200, 300))
