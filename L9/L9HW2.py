# Task 29
# 1.
a = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x+100, a))
print(new_list)

# 2.
new_list1 = list(filter(lambda x: x % 2 == 0, a))
print(new_list1)