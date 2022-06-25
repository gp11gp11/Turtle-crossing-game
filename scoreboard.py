from turtle import Screen, Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(0,250)
        self.write(f"level:{self.level}", align="center", font=("courier",24,"normal"))
       
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("courier",24,"normal"))
        
    def winner(self):
        self.clear()
        self.goto(0,50)
        self.level+=1
        self.update_score()

   