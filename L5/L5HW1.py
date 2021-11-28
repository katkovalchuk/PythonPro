# Task 15

# 14.1
def task1(any_list):
    while True:
        return sum(i for i in any_list)


# 14.2
def task2(any_list):
    x = 0
    while x < len(any_list):
        new_list = [i / 2 if i % 2 != 0 else int(i / 2) for i in any_list]
        return new_list


# 14.3
def task3(any_list):
    length = 0
    while True:
        for i in any_list:
            length += 1
        return length


# 14.4
def task4(any_list, any_number):
    for i in any_list:
        if i == int(any_number):
            return True
    return False


# 14.13
def task13():
    number1 = 1
    while number1 < 11:
        number2 = list(range(1, 11))
        for k in number2:
            print(f"{number1} x {k} = {number1 * k}")
        number1 += 1


# 14.15
def task15():
    score = 0
    print(f"Your score is {score}")
    i = 0
    while i < 10:
        number1 = input("Please enter the first number \n")
        if int(number1) == -1:
            print("Bye!")
            break
        number2 = input("Please enter the second number \n")
        if int(number2) == -1:
            print("Bye!")
            break
        result = input(f"What's the result of {number1} * {number2}? \n")
        if int(result) == int(number1) * int(number2):
            score += 1
            print(f"Correct! \nYour new score is {score}")
        else:
            score += 0
            print(f"Incorrect! \nYour score is  still {score}")
        i += 1


# 14.17
def task17(any_number):
    i = 0
    while i < any_number:
        print('*' * any_number)
        i += 1


# 14.19
def task19(any_number):
    i = 0
    while i < any_number:
        if i % 2 == 0:
            print('*' * any_number)
        else:
            print(' ' + "*" * any_number)
        i += 1


# 14.22
def task22(sum1, increase, months):
    new_sum = sum1
    i = 0
    while i < months:
        new_sum = new_sum * (increase / 100) + new_sum
        i += 1
    return new_sum


# 14.24
def task24(any_number):
    i = 1
    while i <= any_number:
        for j in range(1, i + 1):
            print("*", end="")
        print()
        i += 1