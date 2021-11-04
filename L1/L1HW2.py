import math

# 1. Вычесть из 14 число 7. Результат записать в переменную x. Распечатать содержимое переменной x.
x = 14 - 7
print(x)

# 2. Вычислить остаток от деления 24 на 8. Результат записать в переменную x. Распечатать содержимое переменной x.
x = 24 % 8
print(x)

# 3. Разделить 23 на 6. Результат записать в переменную x. Распечатать содержимое переменной x.
x = 23 / 6
print(x)

# 4. Умножить 11 на 16. Результат записать в переменную x. Распечатать содержимое переменной x.
x = 11 * 16
print(x)

# 5. Возвести в 3-ю степень число 25. Результат записать в переменную x. Распечатать содержимое переменной x.
x = 25 ** 3
print(x)


# 6. Запрограммировать следующую формулу. y и x это переменные. Значение переменной x придумать самостоятельно.

def task6():
    x = 10
    y = 17 * (x ** 2) - 6 * x + 13
    return y


print(task6())


# 7. Запрограммировать следующую формулу. Значение переменной a придумать самостоятельно.
# Результат формулы записать в переменную x.


def task7():
    a = 20
    x = math.sqrt((2 * a + math.sin(abs(3 * a))) / 3.56)
    return round(x, 4)


print(task7())


# 8. Запрограммировать следующую формулу. Значение переменных x y придумать самостоятельно.
# Результат формулы записать в переменную z.


def task8():
    x = 5
    y = 7
    z = (x + ((2 + y) / (x ** 2))) / (y + (1 / math.sqrt((x ** 2) + 10)))
    return round(z, 4)


print(task8())


# 9.
# В подъезде № 1 пятиэтажного жилого дома 15 квартир.
# Определить, на каком этаже этого подъезда находится квартира с заданным номером.
# Номер квартиры содержит переменная x.

# x = apartment number
# y = flor number


def task9(x):
    floors = 5
    apartments = 15
    if x <= 15:
        y = math.ceil((x * floors) / apartments)
        return y
    else:
        return "You have entered incorrect value for the apartment number"


print(task9(2))
print(task9(7))
print(task9(14))
print(task9(48))


# 10. Дано расстояние в сантиметрах в переменной x. Найти число полных метров в нем.


def task10(x):
    y = x / 100
    if x == 1:
        return f"{x} centimeter equals to {y} meters."
    else:
        return f"{x} centimeters equals to {y} meters."


print(task10(1))
print(task10(22))
print(task10(150))
print(task10(2546))


# 11.
# Даны катеты прямоугольного треугольника в переменных a и b.
# Найти его периметр (сумма всех сторон фигуры) и записать его в переменную p.


def task11(a, b):
    if (isinstance(a, str) is True) or (isinstance(b, str) is True):
        return "Incorrect argument has been sent as function parameter. Please send numeric data."
    else:
        c = math.sqrt(a ** 2 + b ** 2)
        p = a + b + c
        return round(p, 4)


print(task11(4, 6))
print(task11(10.7, 34.2))
print(task11("string", "string"))


# 12.
# Известны основания b и с равнобедренной трапеции и её высота h. Вычислить её периметр.
# Справка: У равнобедренной трапеции боковые стороны и углы к основаниям равны.

# d = diagonal
# a = trapezoid side

def task12(b, c, h):
    if (isinstance(b, str) is True) or (isinstance(c, str) is True) or (isinstance(h, str) is True):
        return "Incorrect argument has been sent as function parameter. Please send numeric data."
    else:
        d = math.sqrt(h ** 2 + c ** 2)
        a = math.sqrt(d ** 2 - b * c)
        p = (2 * a) + b + c
        return round(p, 4)


print(task12(4, 10, 15))
print(task12(10, 20, 10))
print(task12("10", "5", "15"))