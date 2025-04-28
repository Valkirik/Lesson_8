class Robot:
    def __init__(self, name, x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"Rpbot {self.name} is on the spot: x - {self.x}, y = {self.y}"


