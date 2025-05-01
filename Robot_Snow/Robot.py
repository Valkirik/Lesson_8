class Robot:
    def __init__(self, name, x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"Rpbot {self.name} is on the spot: x - {self.x}, y = {self.y}"

    @staticmethod
    def move(string: str):
        new_x = 0
        new_y = 0
        for i in list(string.split()):
            if i.capitalize() == "U" :
                new_y += 1
            elif i.capitalize() == "D":
                new_y -= 1
            elif i.capitalize() == "R":
                new_x += 1
            else:
                new_x -= 1

        l = [new_x, new_y]
        for i in l:
            match i:
                case int() as num if num > 5:
                    print("The robot can not move on")
                    return Robot.move(string[:-1])

                case int() as num if num < 0:
                    print("The robot can not move on")
                    return Robot.move(string[:-1])

        return f"The robot on the cell: x = {new_x}, y = {new_y}"

robot_1 = Robot("R2D2", x=0, y=0)
print(robot_1.move("u u  r r d"))


