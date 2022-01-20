# Task 41

import pandas
info = pandas.read_csv('info.csv')
marks = pandas.read_csv('marks.csv')

# 1.
# find out how many people are in df info
info_people = info.shape[0]
merged_table = info.merge(marks, left_on='id', right_on='id2')
no_grades = info_people - merged_table.shape[0]


# 2.
merged_table = info.merge(marks, left_on='id', right_on='id2')

# first resolution will get us all groups average grade in math
all_groups_average = merged_table[['race', 'math']].groupby('race').mean()

# second resolution will get us only group A average grade in math
group_a_average = merged_table.groupby('race')['math'].mean()['group A']


# 3.
merged_table1 = info.merge(marks, left_on='id', right_on='id2', how='outer')
number_of_rows1 = merged_table1.shape[0]


# 4.
merged_table2 = info.merge(marks, left_on='id', right_on='id2', how='left')
number_of_rows2 = merged_table2.shape[0]


# 5.
merged_table3 = info.merge(marks, left_on='id', right_on='id2', how='right')
number_of_rows3 = merged_table3.shape[0]