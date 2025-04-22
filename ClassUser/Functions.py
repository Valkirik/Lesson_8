from Model import User
from ClassAnnotation import UserAnnotation
from random import randint, sample

names = ["Valery", "Slava", "Anna", "Olga", "Pablo"]
surnames = ["Let", "Mar", "Kjds", "Kit", "Pot"]
professions = ["teacher", "policman", "driver", "waiter", "mucision"]
countries = ["Italy", "Israel", "Russia", "USA"]

def get_user() -> UserAnnotation:
    user = User(name=names[randint(0, len(names) - 1)], surname=surnames[randint(0, len(surnames) - 1)], age=randint(1, 100), country=countries[randint(0, len(countries) - 1)], gender="Male/Female", profession=professions[randint(0, len(professions) - 1)])
    return user








