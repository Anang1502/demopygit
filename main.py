from math1 import addition
from person import Person

name = "Anang Raj"
name2 = "Manu"


def hello(name: str):
    print(name.upper())

def hello2(name: str):
    print(name.upper())


def alex_method(name):
    p = Person(name)
    print(p)

if __name__ == '__main__':
    # TODO: Fix Bug
    # TODO: Implement tests
    print("Pycharm is AWESOME, isn't it!!")
    print("Pycharm is AWESOME")
    print("Pycharm")
    print(addition(2, 2))
    alex_method("Ali")
