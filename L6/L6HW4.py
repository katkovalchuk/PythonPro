# Task 21
# 13.1
def task1(x):
    if not isinstance(x, int):
        raise Exception("I can take only numbers")
    else:
        if x <= 34:
            print("Kat")
        else:
            print("Iryna")


# 13.2
def task2(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise Exception("I can take only numbers")
    else:
        if x + y == 5:
            return (x + y) / 2
        else:
            return x + y


# 13.4
def string_length(test_string):
    if not isinstance(test_string, str):
        raise Exception("I print only strings")
    else:
        list_string = list(test_string)
        if len(list_string) < 5:
            print(test_string)
        else:
            print("The line is too big, I'm tired")


# 13.6
def get_number(message):
    while True:
        try:
            return int(input(message))
        except Exception:
            continue


def main():
    number1 = get_number("Please enter the number.\n")
    number2 = get_number("Please enter the other number\n")
    result = input(f"How much will be {number1} multiplied by {number2}?\n")
    correct_result = int(number1) * int(number2)
    if int(result) == correct_result:
        print(True)
    else:
        print(False)


# 13.9
def my_func5():
    name = input("What is your name?\n")

    if name == "Jack" or name == "Bob":
        print("Hi there!")
    elif name == "Brian":
        print("Hello Brian!")
    else:
        raise Exception("Sorry, but I don't know you.")


# 14.1
def task141(any_list):
    s = 0
    for i in any_list:
        try:
            if isinstance(i, int):
                s += i
        except Exception:
            continue
    return s


# 14.5
def task5(any_list):
    sum1 = 0
    average = 0
    if len(any_list) == 0:
        raise Exception("Can't count the average for the empty list")
    else:
        for i in any_list:
            sum1 += i
            average = sum1 / len(any_list)
        return average


# 14.6
def task6(any_list):
    max_value = 0
    if len(any_list) == 0:
        raise Exception("List is empty")
    else:
        for n in any_list:
            if n > max_value:
                max_value = n
        return max_value


# 14.8
def task8(any_list):
    new_list = []
    for i in any_list:
        try:
            if isinstance(i, int):
                if i % 2 ==0:
                    new_list.append(i)
        except Exception:
            continue
    return new_list