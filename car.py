from turtle import Screen, Turtle
import random
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.colours = ["red","blue", "yellow", "green", "brown", "black"]
        self.scale = 0
    
    def make_car(self):
        rand = random.randint(1,5)
        if rand == 3:
            car = Turtle("square")
            car.shapesize(stretch_wid = 1,stretch_len = 2)
            car.color(random.choice(self.colours))
            car.penup()
            self.hideturtle()
            random_y = random.randint(-250,250)
            car.goto(350, random_y)
            self.cars.append(car)
    
    def move_car(self):
        for car in self.cars:
            speed = random.randint(5,30) + self.scale
            car.backward(speed)
    def levelup_car(self):
            self.scale += 20
            