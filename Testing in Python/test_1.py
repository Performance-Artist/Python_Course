import pytest
from operator import truediv

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.capit()

    def capit(self):
        self.name.capitalize()
        self.surname.capitalize()

names = [('john', 'smith'), ('Joe', 'white'), ('Alice', 'michelson')]

def test_capitalize_feature():
    global names
    for name in names:
        person = Person(name[0], name[1])
        true = person.name + ' ' + person.surname
        true.capitalize()
        assert person.name + ' ' + person.surname == true, "Name capitalization doesn't work"