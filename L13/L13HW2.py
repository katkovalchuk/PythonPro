# Task 40
import pandas

df = pandas.read_csv('titanic.csv')
print(df)
print(df.columns)

index = df.index
number_of_rows = len(index)
print(number_of_rows)

male_count = df['Sex'].value_counts()['male']
print(male_count)
df.groupby('Sex')['Sex'].count()  # can count both sexes at the same time

survived = df['Survived'].value_counts()[1]
percentage_survived = (survived * 100) / number_of_rows
print(round(percentage_survived, 2))


def on_board():
    percentage_of_male = (male_count * 100) / number_of_rows
    if percentage_of_male > 50:
        print(f"There were more men on the board with percentage of {round(percentage_of_male, 2)}.")
    else:
        print(f"There were more women on the board with percentage of {round(100 - percentage_of_male, 2)}.")


survived_men = df.groupby('Sex')['Survived'].sum()['male']
percentage_survived_men = (survived_men * 100) / survived
print(round(percentage_survived_men, 2))


survived_class = df[['Pclass', 'Survived']].groupby('Pclass').mean()