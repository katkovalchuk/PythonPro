# Task 12

# 1.
def welcome():
    customers_name = input("What is your name?\n")

    print(f"Hello, {customers_name}! Welcome to our website!")


# 2.
def weight_index():
    height = input("What is your height in meters?\n")
    weight = input("And what is your weight in kilograms?\n")

    index = int(weight) / float(height) ** 2

    return f"Your weight index is {round(index, 4)}"
