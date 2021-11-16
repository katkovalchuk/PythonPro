# Task 10.
def task1(a, b):
    c = a + b
    return c


def task2(a):
    c = a * 4
    return c


def task3(a, b, c):
    d = (a + b + c) / 3
    return d


def task4():
    return 4


def task5(x):
    d = x % 5
    return d


def task6(a, b):
    c = a + b
    my_dict = {'key1': a, 'key2': b, 'key3': c}
    return my_dict


# Task 7


my_list1 = [2, 5, 7, 8, 12]
my_list2 = [1, 2, 4]
my_list3 = [2, 5]


def task7(my_list):
    a = 8 in my_list
    b = 4 in my_list
    if a is True or b is True:
        return True
    else:
        return False


# Task 8

my_list4 = [10, 20, 30, 40]
my_list5 = [100, 200, 300, 400]


def task8(list1, list2):
    a = list1[1] / list2[0]
    return a


# Task 9

my_string = "this is my string"


def task9(any_string):
    new_string = any_string.replace(" ", "privet")
    return new_string


# Task 10

my_string = "this is my string"


def task10(any_string):
    a = any_string.split(" ")
    return a[1]


# Task 11
my_list6 = [3, 5, 6, 8, 0]


def task11(any_list):
    any_list[0] = 4
    return any_list


# Task 12
my_dict = {'a': 23, 'b': 45, 'c': 88}


def task12(any_dict):
    any_dict['a'] = 86
    return any_dict


# Task 13
def task13(any_dict):
    del any_dict['b']
    return any_dict


# Task 14
# If there's a better solution, would love to hear

my_list7 = [12, 44, 66, 77]


def task14(any_list):
    c = any_list[1] + 33
    any_list[1] = c
    return any_list


# Task 15
def task15(any_list):
    c = any_list[0] + any_list[-1]
    any_list.append(c)
    return any_list


# Task 16
my_dict2 = {'a': 65, 'b': 93}


def task16(any_dict):
    any_dict['c'] = any_dict['a'] + 45
    return any_dict


# Task 17
my_list8 = [21, 99, 84, 15]


def task17(any_list):
    any_list[0] = any_list[1]
    return any_list


# Task 18
my_dict3 = {'a': 55, 'b': 43}


def task18(any_dict, any_number):
    del any_dict['a']
    any_dict['c'] = any_number
    return any_dict


# Task 19
my_list9 = [12, 13, 14, 15, 16, 17, 18, 19]


def task19(any_list):
    new_list = [any_list[0], any_list[-1]]
    return new_list


# Task 20
my_dict4 = {'a': 32, 'b': 54, 'c': 18, 'm': 78}


def task20(any_dict):
    new_list = [any_dict['b'], any_dict['m']]
    return new_list


# Task 21
my_list10 = [1, 2, 3, 4]


def task21(any_list, any_number):
    any_list.insert(0, any_number)
    return any_list


# Task 22
my_string3 = "this is my string"


def task22(any_string):
    new_list = any_string.split(" ")
    a = len(new_list)
    return a


# Task 23
my_string4 = "Great Britain"
my_string5 = "London is the capital of Great Britain"


def task23(any_string):
    new_string = ""
    words = any_string.split(" ")
    if len(words) <= 2:
        words_reversed = list(reversed(words))
        new_string = " ".join(words_reversed)
        return new_string
    else:
        return "This function excepts only 2 words strings."
