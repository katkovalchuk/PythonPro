# Task 13

# 1.
def task1():
    number = input("Please enter any number.\n")

    if int(number) <= 34:
        print("Kat")
    else:
        print("Iryna")


# 2.
def task2():
    number1 = input("Please enter any number.\n")
    number2 = input("Please enter one more number.\n")

    total = int(number1) + int(number2)

    if total == 5:
        return total / 2
    else:
        return total


# 3.
def distance():
    km = input("Please enter distance in kilometres.\n")
    ft = input("Please enter distance in feet.\n")

    #  1km = 3280.84ft
    km_to_feet = int(km) * 3280.84

    if km_to_feet > int(ft):
        print("Distance in kilometres is longer.")
    elif km_to_feet < int(ft):
        print("Distance in feet is longer.")
    else:
        print("Distance is equal.")


# 4.
def string_length():
    test_string = input("Please enter the line.\n")
    list_string = list(test_string)

    if len(list_string) < 5:
        print(test_string)
    else:
        print("The line is too big, I'm tired")


# 5.
def my_func():
    number1 = input("Please enter the number.\n")
    number2 = input("Please enter the other number\n"")

    if int(number1) > int(number2):
        print(int(number1) + int(number2))
    else:
        print(int(number1) - int(number2))

        # 6.


def my_func2():
    number1 = input("Please enter the number.\n")
    number2 = input("Please enter the other number\n")
    result = input(f"How much will be {number1} multiplied by {number2}?")

    correct_result = int(number1) * int(number2)

    if int(result) == correct_result:
        print(True)
    else:
        print(False)


# 7.
def my_func3():
    question = input("What city is the capital of the Republic of Belarus?\n Please choose the correct option:\n"
                     "a. Bobruysk\n"
                     "b. London\n"
                     "c. Minsk\n")

    if question == "c" or question == "c." or question == "c. Minsk" or question == "Minsk" or question == "c.Minsk":
        print(True)
    else:
        print(False)


# 8.
def my_func4(any_string):
    word1 = input("Which word should be replaced?\n")
    word2 = input("What this word should be replaced with?\n")

    new_string = any_string.replace(word1, word2)

    return new_string


# 9.
# With all do respect, I have changed the names and output for more professional language.
# Logic is intact.

def my_func5():
    name = input("What is your name?\n")

    if name == "Jack" or name == "Bob":
        print("Hi there!")
    elif name == "Brian":
        print("Hello Brian!")
    else:
        print("Sorry, but I don't know you.")


# 10.
def my_func6(any_number):
    str_number = str(any_number)

    if len(str_number) > 2 or len(str_number) <2:
        print("Incorrect number")
    else:
        if str_number[0] > str_number[1]:
            return 1
        elif str_number[0] < str_number[1]:
            return 2
        else:
            return 0


# 11.
def my_func7(any_number):
    str_number = str(any_number)

    if type(any_number) == int:
        if len(str_number) > 4 or len(str_number) < 4:
            print("Incorrect number")
        else:
            if str_number == str_number[::-1]:
                print("This number is palindrome!")
            else:
                print("This number is NOT a palindrome.")
    else:
        print("The value you've entered is not a number.")


# 12.
def my_func8(a, b):
    if type(a) == int and type(b) == int and a > b:
        if a % b == 0:
            print(f"{b} is a divider for {a}.")
        else:
            print(f"{b} is not a divider for {a}.")
    else:
        print("You gave incorrect arguments to the function")


# 13.
# Small comment here, that the task itself could have been set in different example with the same logic.


def my_func9(a, b, d):
    if a == b:  #if the window is a square
        if d <= (a - 2):  #if window is a square, then a == b
            return True
        else:
            return False
    elif b > a:  #if the window is rectangle
        if d <= (a -2):
            return True
        else:
            return False
    else:  #if a > b
        if d <= (b - 2):
            return True
        else:
            return False


# 14.
import math

def my_func10(a, b, c):
    a1 = float(a)
    b1 = float(b)
    c1 = float(c)

    square_root = []

    d = b1 ** 2 - 4 * a1 * c1
    
    if a != 0:
        if d > 0:
            x1 = (-b1 + math.sqrt(d)) / (2 * a1)
            x2 = (-b1 - math.sqrt(d)) / (2 * a1)
            square_root.extend([round(x1, 4), round(x2, 4)])
            return square_root
        elif d == 0:
            x = -b1 / (2 * a1)
            square_root.extend([round(x, 4)])
            return square_root
        else:
            return square_root
    else:
        print("This is not a square equation")


# 15.
def my_func11(x):
    return x ** 2


# 16.
def my_func12(x):
    return x ** 2 + 5


# 17.
import datetime

def my_func13(day, month, year):
    try:
        check_date = datetime.datetime(year, month, day)
        print("Yes")
    except ValueError:
        print("No")


# 18.
def my_func14(n):
    if 1 < n <= 99 and isinstance(n, int) is True:
        print(f"I'm {n} years old")  #plural
    elif n == 1:
        print(f"I'm {n} year old")  #singular
    else:
        print("You've entered incorrect value in the function")