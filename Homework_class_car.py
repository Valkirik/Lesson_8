class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def __str__(self):
        return f"{self.type} {self.color} {self.year}"

    def get_start(self):
        return "the car is ready to go"

    def get_stop(self):
        return "the cat stoped"



