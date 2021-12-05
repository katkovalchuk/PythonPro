# Task 25
# 1.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Kat", 26)
p2 = Person("Iryna", 42)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


# 2.
class Tree:
    def __init__(self, name, high, age):
        self.name = name
        self.high = high
        self.age = age


t1 = Tree("Oak", 12, 5)
t2 = Tree("Maple", 7, 3)

print(t1.name)
print(t1.age)
print(t1.high)
print(t2.name)
print(t2.age)
print(t2.high)


# 3.
class House:
    def __init__(self, location, square):
        self.location = location
        self.square = square


h1 = House("street", 45)
h2 = House("boulevard", 100)

print(h1.location)
print(h1.square)
print(h2.location)
print(h2.square)


# 4.
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


b1 = Book("The Subtle Art of not giving a F*ck", "Mark Manson")
b2 = Book("Beartown", "Fredrik Backman")

print(b1.name)
print(b1.author)
print(b2.name)
print(b2.author)


# 5.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


d1 = Date(14, 3, 2019)
d2 = Date(25, 2, 2021)

print(d1.day)
print(d1.month)
print(d1.year)
print(d2.day)
print(d2.month)
print(d2.year)


# 6.
class EnvelopeWithLetter:
    def __init__(self, sender, adressee):
        self.sender = sender
        self.adressee = adressee


e1 = EnvelopeWithLetter("friend", "me")
e2 = EnvelopeWithLetter("mum", "niece")

print(e1.sender)
print(e1.adressee)
print(e2.sender)
print(e2.adressee)