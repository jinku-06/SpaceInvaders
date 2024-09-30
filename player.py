import turtle


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("Gifs/player.gif")
        self.shape("Gifs/player.gif")
        self.penup()
        self.speed(0)
        self.setposition(0, -300)
        self.setheading(90)

    def move_left(self, player_speed: int):
        x = self.xcor()
        x -= player_speed
        if x < -360:
            x = -360
        self.setx(x)

    def move_right(self, player_speed: int):
        x = self.xcor()
        x += player_speed
        if x > 360:
            x = 360

        self.setx(x)
