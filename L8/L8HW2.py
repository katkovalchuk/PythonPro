# Task 26
# 1.
class Tree:
    def __init__(self, name, high, age):
        self.name = name
        self.high = high
        self.age = age

    def growth(self, how_much):
        self.high += how_much
        return self.high


# 2.
class Person:
    def __init__(self, name, age, eaten_candy):
        self.name = name
        self.age = age
        self.eaten_candy = eaten_candy

    def eat_candies(self):
        print(f"{self.name} has eaten {self.eaten_candy} candies at the age of {self.age}.")


# 3.
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def print_pages(self, page):
        for i, v in enumerate(self.pages):
            if (i+1) == page:
                print(v)
                break
            else:
                continue


b1 = Book("The Subtle Art of not giving a F*ck", "Mark Manson", ["aaaaa", "bbbbb", "ccccc"])


# 4.
class EnvelopeWithLetter:
    def __init__(self, sender, adressee, letter):
        self.sender = sender
        self.adressee = adressee
        self.letter = letter

    def sign(self):
        self.letter.append(f"Sincerely yours, {self.sender}")


# 5.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def add_days(self, days):
        self.day += days
        if self.day > 30:
            number = self.day
            self.day = number % 30
            self.month = self.month + int(number / 30)
        return self.day
