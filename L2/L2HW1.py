# Task 8
# 1.
x = 9 > 5
print(x)

y = 10 <= 10
print(y)

a = 5 > 10
print(a)

b = 18 <= 5
print(b)

# 2.
x = 6
y = 8
print(x != y)

if 5 != 10:
    print(False)

x = 10 != 10
print(x)

y = 15 == 15
print(y)

# 3.
my_dict = {"name1": "Diana", "name2": "Anna", "name3": "Jack"}

not_false = "name1" in my_dict
print(not_false)

not_true = "name8" in my_dict
print(not_true)

# 4.
my_list = [1, 2, 3, 4, 5]

if 1 in my_list:
    print('True Story')

x = 6 in my_list
print(x)

# 5.
my_string = "this is my string"

a = "this" in my_string
print(a)

b = "I" in my_string
print(b)


# Task 9.
t1 = 10 > 1 and 8 < 80
t2 = 15 >= 15 and 9 <= 9
t3 = 12 != 2 and 5 == 5
f1 = 1 > 10 and 80 > 8
f2 = 15 >= 15 and 9 < 9
f3 = 12 != 12 and 5 != 5
print(t1, t2, t3, f1, f2, f3)

# Task10.
t10 = 10 > 1 or 8 > 80
t20 = 15 >= 15 or 9 >= 9
t30 = 12 != 12 or 5 == 5
f10 = 60 > 60 or 48 != 48
f20 = 18 < 10 or 6 == 99
f30 = 78 != 78 or 15 < 3
print(t10, t20, t30, f10, f20, f30)