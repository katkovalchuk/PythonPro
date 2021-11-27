# Task 14
import math
import heapq


# 1.
def task1(any_list):
    s = 0
    for i in any_list:
        s += i
    return s


# 2.
def task2(any_list):
    new_list = []
    for i in any_list:
        if i % 2 != 0:
            new_list.append(i / 2)
        else:
            c = int(i / 2)
            new_list.append(c)
    return new_list


# 3.
def task3(any_list):
    length = 0
    for i in any_list:
        length += 1
    return length


# 4.
def task4(any_list, any_number):
    for i in any_list:
        if i == int(any_number):
            return True
    return False


# 5.
def task5(any_list):
    average = sum(any_list) / len(any_list)
    return average


# 6.
def task6(any_list):
    max_value = 0
    for n in any_list:
        if n > max_value:
            max_value = n
    return max_value


# 7.
def task7(any_list):
    min_value = any_list[0]
    for n in any_list:
        if n < min_value:
            min_value = n
    return min_value


# 8.
def task8(any_list):
    new_list = [i for i in any_list if i % 2 == 0]
    return new_list


# 9.
def task9(any_list):
    new_list = [i for i in any_list if i % 2 != 0]
    return new_list


# 10.
def task10(any_list1, any_list2):
    new_list = [i for i in any_list1 if i in any_list2]
    return new_list


# 11.
def task11(any_list1, any_list2):
    new_list = [i for i in any_list1 if i not in any_list2]
    return new_list


# 11.2
# The task is not comprehensive enough to solve it with range(). Need more explanation.
# Also, wanted to mention that programming is meant to simplify the task, not make it more complicated.

def task112(any_number1, any_number2):
    new_list = [any_number1, any_number2]
    result = math.prod(new_list)
    return result


# 12.
def task12(x, y):
    return int(math.pow(x, y))


# 13.
# I'm not sure how to separate each block of the table (x1-10).
# If you know how to create spaces between them - please let me know.
def task13():
    number1 = number2 = list(range(1, 11))
    for i in number1:
        for k in number2:
            print(f"{i} x {k} = {i * k}")


# 14
def task14(any_list):
    new_list = []
    for i in any_list:
        new_list.append(str(i))
    for i, v in enumerate(new_list):
        new_length = len(new_list[0])
        print(" " * (3 + (new_length - len(new_list[i]))) + v)


# 15.
def task15():
    score = 0
    print(f"Your score is {score}")
    for i in range(10):
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


# 16.
# elegant.
def task16(any_list):
    return heapq.nlargest(2, any_list)


# okay, okay. here you go with your long and "for-looped" answer.
def task161(any_list):
    max_value = any_list[0]
    second_largest = any_list[0]
    for i in range(len(any_list)):
        if any_list[i] > max_value:
            max_value = any_list[i]
    for i in range(len(any_list)):
        if any_list[i] > second_largest and any_list[i] != max_value:
            second_largest = any_list[i]
    return f"Max value is {max_value}, next value in line is {second_largest}."


# 17.
# imho would be better if we learned turtle
def task17(any_number):
    for i in range(any_number):
        print('*' * any_number)


# 18.
def task18(any_number):
    for i in range(any_number):
        for j in range(any_number):
            if i == 0 or i == any_number-1 or j == 0 or j == any_number-1:
                print('*', end="")
            else:
                print(' ', end="")
        print()


# 19.
def task19(any_number):
    for i in range(any_number):
        if i % 2 == 0:
            print('*' * any_number)
        else:
            print(' ' + "*" * any_number)


# 20.
def task20(any_number1, any_number2):
    if any_number1 < any_number2:
        for i in range(any_number1, any_number2+1):
            if i % 2 == 0:
                print(i)
    else:
        return "You've entered incorrect numbers"


# 21.
def task21(any_number):
    fact = 1
    if any_number < 0:
        print("Sorry, factorial can't be found from negative numbers")
    elif any_number == 0:
        print("The factorial of 0 equals 1.")
    else:
        for i in range(1, any_number+1):
            fact = fact * i
        print(f"The factorial of {any_number} is {fact}.")


# 22.
def task22(sum1, increase, months):
    new_sum = sum1
    for i in range(months):
        new_sum = new_sum * (increase / 100) + new_sum
    return new_sum


# 23.
def task23(any_number):
    if any_number <= 1:
        return False
    for i in range(2, int(math.sqrt(any_number) + 1)):
        if any_number % i == 0:
            return False
    return True


# 24.
def task24(any_number):
    for i in range(1, any_number + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()


# 25.
def task25(any_number):
    space = 2 * any_number - 2
    for i in range(0, any_number):
        for j in range(0, space):
            print(end=" ")
        space = space - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
    space = any_number - 2
    for i in range(any_number, -1, -1):
        for j in range(space, 0, -1):
            print(end=" ")
        space = space + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")