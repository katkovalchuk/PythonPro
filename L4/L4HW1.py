# Task 14
import math


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


# 14 unfinished
def task14(any_list):
    for i, v in enumerate(any_list):
        c = len(any_list)
        next_number = " " * c + str(any_list[i])
        print(next_number)

