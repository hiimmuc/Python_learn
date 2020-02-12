class Question:
    def __init__(self, promts, answer):
        self.promts = promts
        self.answer = answer


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class Chef:
    def make_chicken(self):
        print("making chicken")

    def make_salad(self):
        print("making salad")


class Vietnamese_chef(Chef):
    def make_dishes(self):
        print("making tonight dishes")


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_coordinate(self):
        print(f"the coordinate of this point is ({self.x},{self.y},{self.z})")
