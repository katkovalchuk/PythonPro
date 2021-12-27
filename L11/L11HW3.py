# Task 35
import re
# 1.
re.match(r"^a\d+c$", "a23c")

# 2.
re.match(r"^a(\d+|\d*)c$", "ac")


# 3.
def get_login(email):
    pattern = r"^\w+@\w+\.(com|net)$"
    if re.search(pattern, email):
        print(email.split("@")[0])
    else:
        raise Exception("You have entered incorrect email")


# 4.
re.match(r"^<\w+>(\w+)</\w+>$", "<tag>text</tag>").groups()


# 5.
def time_checker(time):
    pattern = r"^\d{4}-\d{2}-\d{2}\s\d\d:(\d\d):\d\d$"
    if re.match(pattern, time).groups():
        return time[0]
    else:
        print("I don't understand")


# 6.
def calc(any_expression):
    pattern = r"^(-?\d+)\s(\+|\*|/|-)\s(-?\d+)$"
    if re.match(pattern, any_expression).groups():
        return eval(any_expression)
    else:
        print("You've entered incorrect string to the function")