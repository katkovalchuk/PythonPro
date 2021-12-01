# Task 17

# 1.
ls = [4, [7, 8], 6]

a, (x, b), y = ls
print(x, y)


# 2.
ls = [ (3, [9, 1]), [(23,43), [5, 4]] ]


def fn():
    new_list = []
    for (_ , [x, _]) in ls:
        new_list.append(x)
    return sum(new_list)