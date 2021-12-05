# Task 27
# 1.
import math


class Building:
    def __init__(self, floors):
        self.floors = floors

    def which_floor(self, floor):
        if floor <= self.floors:
            print(f"You're on {floor} floor")
        else:
            print("You've got incorrect floor number")


class Moll(Building):
    def __init__(self, floors, elevators):
        self.elevators = elevators
        super().__init__(floors)

    def elevator_floor(self):
        # for 1 floor - 2 elevators
        result = math.ceil(self.elevators / 2)
        print(f"This {self.elevators} elevator is on {result} floor.")


class School(Building):
    def __init__(self, floors, cabinets):
        self.cabinets = cabinets
        super().__init__(floors)

    def cabinet_floor(self):
        # for 1 floor - 5 cabinets
        result = math.ceil(self.cabinets / 5)
        print(f"This {self.cabinets} cabinet is on {result} floor.")


# 2.
class Factorial:
    def __get_factorial(self, a):
        fact = 1
        if a < 0:
            print("Sorry, factorial can't be found from negative numbers")
        elif a == 0:
            print("The factorial of 0 equals 1.")
        else:
            for i in range(1, a + 1):
                fact = fact * i
            print(f"The factorial of {a} is {fact}.")

    def calculate(self, a):
        return self.__get_factorial(a)


# 3.
class Bank:
    def __init__(self, deposits):
        self.deposits = deposits
    def __add__(self, other):
        new_bank = self.deposits + other.deposits
        return Bank(new_bank)