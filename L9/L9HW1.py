# Task 28
# 1.
import math


def cap_first(func):
    def wrapper(*args):
        f_call = func(*args)
        result = f_call.capitalize()
        return result
    return wrapper


@cap_first
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]


print(swap_words("words magic"))


# 2.
def two_times(fn):
    def wrapper(*args):
        return fn(fn(*args))
    return wrapper


@two_times
def mult_on_2(ls):
    result = []
    for x in ls:
        result.append(x * 2)
    return result


print(mult_on_2([1, 2, 3, 4, 5]))


# 3.
def checker(fn):
    def wrapper(*args):
        for i in args:
            if i < 0:
                print("You can't pass negative numbers")
                return -1
            else:
                fn_call = fn(*args)
                return fn_call
    return wrapper


@checker
def my_sqrt(x):
    return math.sqrt(x)


print(my_sqrt(-3))
print(my_sqrt(2))