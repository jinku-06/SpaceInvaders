from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=0.25, stretch_len=2)
        self.hideturtle()
        self.state = "ready"

    def fire(self, x, y):
        self.state = "fire"
        self.setposition(x, y + 10)
        self.showturtle()

    def move(self, bullet_speed):
        if self.state == "fire":
            y = self.ycor()
            y += bullet_speed
            self.sety(y)

            if self.ycor() > 350:
                self.hideturtle()
                self.state = "ready"

    def reset(self):
        self.hideturtle()
        self.state = "ready"
