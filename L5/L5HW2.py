# Task 16
from functools import reduce


# 1.
def fn1(x):
    if x > 100:
        return x * 2
    else:
        return x / 3


list(map(fn1, [100, 200, 300]))


# 2.
def fn2(any_number):
    return any_number % 2 == 0


list(filter(fn2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 3.
def fn3(a, b):
    return a + b


reduce(fn3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# 4.
def map_func(any_fn, any_iter):
    new_list = [any_fn(i) for i in any_iter]
    return new_list


map_func(fn1, [100, 200, 300])


# 5.
def filter_func(any_fn, any_iter):
    new_list = []
    for i in any_iter:
        if any_fn(i) is True:
            new_list.append(i)
        else:
            continue
    return new_list


filter_func(fn2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# 6.
def increment(m):
    return m + 4


def fn(another_fn, x, z):
    for _ in range(z):
        x = another_fn(x)
    return x


print(fn(increment, 6, 2))


# 7.
my_list = [400, 15, 1020, 65]
reduce(max, my_list)
