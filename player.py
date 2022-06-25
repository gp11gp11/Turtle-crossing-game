from turtle import Screen, Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        
        self.goto(0,-280)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def levelup(self):
        self.goto(0,-280)