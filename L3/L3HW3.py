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
