# Task 24
# 1.
required_args = (1, 7)
default_args = {"a": 2, "c": 4}


def fn1(*args):
    args_sum = 0
    for i in args:
        args_sum += i
    return args_sum


fn1(*required_args)


# 2.
def fn2(**kwargs):
    kwargs_mult = 1
    for number in kwargs.values():
        kwargs_mult *= number
    return kwargs_mult


fn2(**default_args)


# 3.
def fn3(a, b, **kwargs):
    result = 0
    for i in kwargs.values():
        result += i
    return result + a + b


fn3(*required_args, **default_args)


# 4.
def fn4(*args, a = 5, c = 9):
    result = 1
    for i in args:
        result *= i
    return result * a * c


fn4(*required_args, **default_args)


# 5.
def fn5(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for v in kwargs.values():
        result += v
    return result


fn5(*required_args, **default_args)