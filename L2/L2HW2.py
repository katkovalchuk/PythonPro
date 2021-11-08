# Task 5.
ls_1 = [4, 15, 5]
y = ls_1[0]
print(y)


ls_2 = [6, 16, 9, 11, 16]
ls_2.append(15)
print(ls_2)


ls_3 = [10, 18, 20]
m = len(ls_3)
print(m)

# additional solution
m1 = 0
for i in ls_3:
    m1 += 1

print(m1)


ls_4 = [7, 5, 16, 5, 1]
k = ls_4 + [3, 12, 9, 11, 14, 5]
print(k)


ls_5 = [14, 18, 16, 19, 19]
ls_5[4] = 14
# if you meant 4th index it will work. but if you meant 4th item (how people count) - it should be ls_5[3]
print(ls_5)


ls_6 = [11, 2, 4, 13]
c = ls_6[1:3]
print(c)


ls_7 = [15, 18, 12, 12, 13]
v = 12 in ls_7
print(v)

# additional solution
v = None
if 12 in ls_7:
    v = True
else:
    v = False
print(v)


ls_8 = [4, 5, 4, 2]
ls_8.append(5)
print(ls_8)


ls_9 = [9, 4, 4, 15, 20]
ls_9[3] = 18
# if you meant 3d index it will work. but if you meant 3d item (how people count) - it should be ls_9[2]
print(ls_9)


# Task 6.
s_1 = 'раздвинув басом ветра вой:'
k = s_1.replace('ветра', 'ваш')
print(k)


s_2 = 'ИЗ УЛИЦЫ В УЛИЦУ'
w = s_2[9]  # same comment as above
print(w)


s_3 = 'а с запада падает красный снег'
v = s_3[2]
print(v)

s_4 = 'как святыню, на руках понесут'
h = 'хочет,' in s_4
print(h)


s_5 = 'Морей неведомых далеким пляжем'
r = s_5.split(" ")
print(r)


s_6 = 'плыла, изгибаясь, дверями влекома;'
n = s_6.replace('плыла,', 'глаза.')
print(n)


s_7 = 'Ты зеленые весны идешь насиловать!'
q = s_7[14]  # same comment
print(q)


s_8 = 'Дай исцелую твою лысеющую голову'
g = s_8[17:25]
print(g)

# additional solution
g1 = s_8.split(" ")
g = g1[3]
print(g)


# Task 7.
d = {'a': 1, 'b': 3, 'c': 12}

# 1
d['m'] = 6
print(d)

# 2
del d['b']
print(d)

# 3
d['b'] = 20
print(d)

# 4
a = d['b']
print(a)

# 5
d['h'] = 18
print(d)

# 6
del d['a']
print(d)

# 7
d['b'] = 11
print(d)

# 8
a = d['c']
print(a)

# 9
d['n'] = 0
print(d)

# 10
del d['b']
print(d)

# 11
d['b'] = 14
print(d)

# 12
a = d['c']
print(a)

# 13
d['y'] = 88
print(d)