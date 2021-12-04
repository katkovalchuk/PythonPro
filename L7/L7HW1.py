# Task 22
# 1.
def fn1(a, b=7):
    return a + b


fn1(4, 8)
fn1(6)


# 2.
def fn2(any_list, default_list=[3, 5, 7]):
    return any_list + default_list


fn2([1, 2, 3], [4, 5, 6 ])
fn2([1, 2, 3])


# 3.
def fn3(any_number, number2 = 5, def_dict = {"d": 1, "b": 2, "divisor": 3}):
    return (any_number + number2) / def_dict["divisor"]


fn3(4, 6, {"a": 2, "b": 4, "divisor": 6})
fn3(3)
