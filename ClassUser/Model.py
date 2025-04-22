from random import randint
from typing import NamedTuple
from ClassAnnotation import UserAnnotation

names = ["Valery", "Slava", "Anna", "Olga", "Pablo"]
surnames = ["Let", "Mar", "Kjds", "Kit", "Pot"]
professions = ["teacher", "policman", "driver", "waiter", "mucision"]
countries = ["Italy", "Israel", "Russia", "USA"]


class User:
    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} - {self.profession}"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.age} - {self.profession}"

    def get_birthyear(self):
        return f"{self.name} {self.surname} was born in {2025 - self.age}"

    def get_email(self):
        return f"{str(self.name).lower()}{str(self.surname).lower()}{str(self.age)}@mail.ru"

def get_user() -> UserAnnotation:
    user = User(name=names[randint(0, len(names) - 1)], surname=surnames[randint(0, len(surnames) - 1)], age=randint(1, 100), country=countries[randint(0, len(countries) - 1)], gender="Male/Female", profession=professions[randint(0, len(professions) - 1)])
    return user

d = get_user()
print(d.get_birthyear())
print(get_user().get_birthyear())
