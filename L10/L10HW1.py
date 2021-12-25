# Task 31
import random

# 1.
x = None
count = 0
while x != '5':
    x = input("Menu:\n1.Add new number.\n2.Get whole list of numbers.\n3.Edit name or number\n"
              "4.Search contact by name or number\n5.Exit\n")
    if x == '1':
        with open('data.txt', 'a') as f:
            name = input("Please enter first name and last name:\n") + " "
            count += 1
            f.write(str(count) + ". " + name)
            number = input("Please enter the phone number:\n") + " "
            f.write(number + "\n")
        print("This person was saved to your address book")
    elif x == '2':
        try:
            with open('data.txt', 'r') as file:
                data = file.read().split("\n")
        except FileNotFoundError:
            print("There's no numbers in the list. Please add new number first.")
            data = []
        for y in data:
            print(y)
    elif x == '3':
        with open('data.txt', 'r') as f:
            lines = f.readlines()  # list
            try:
                which_person = input("Which person do you want to change?\n")
                changing_line = lines[int(which_person)-1]  # str
                changing_line_l = changing_line.split(" ")  # list
                what_to_change = input("What do you want to change: name or number?\n")
                if what_to_change == "name":
                    new_value = input("Please enter the new name\n")
                    changing_line_l[1] = new_value.split(" ")[0]
                    changing_line_l[2] = new_value.split(" ")[1]
                    new_content = " ".join(changing_line_l)
                    lines[int(which_person) - 1] = new_content
                    with open('data.txt', 'w') as file:
                        for x in lines:
                            file.write(x)
                    print("Name has been successfully changed!")
                elif what_to_change == "number":
                    new_value = input("Please enter the new number\n")
                    changing_line_l[3] = new_value
                    new_content = " ".join(changing_line_l)
                    lines[int(which_person) - 1] = new_content
                    with open('data.txt', 'w') as file:
                        for x in lines:
                            file.write(x)
                    print("Number has been successfully changed!")
                else:
                    print("Please choose between name or number. Please try again.")
            except IndexError:
                print("You have entered incorrect person number. Please try again.")
    elif x == '4':
        with open('data.txt', 'r') as f:
            lines = f.readlines()  # list
            search_type = input("Do you want to search by name or by number\n")
            if search_type == "name":
                search_name = input("Please enter the name you want to search\n")
                found = False
                for x in lines:
                    if search_name in x:
                        print(f"Contact found: {x}")
                        found = True
                        break
                if not found:
                    print("There's no such contact in the list")
            elif search_type == "number":
                search_number = input("Please enter the number to search\n")
                found = False
                for x in lines:
                    if search_number in x:
                        print(f"Contact found: {x}")
                        found = True
                        break
                if not found:
                    print("There's no such contact in the list")
            else:
                print("Please choose between name or number. Please try again.")
print('Bye!')


# 2.
x = None
count = 0
while x != '5':
    x = input("Menu:\n1.Release new credit card.\n2.Cash money from the credit card.\n3.Add money to credit card.\n"
              "4.View credit card balance\n5.Exit\n")
    if x == '1':
        with open('atm.txt', 'a') as f:
            password = input("Please enter the new password\n")
            if len(password) < 5:
                print("This password is too small. Please try again.")
            else:
                number = random.randint(1000000000000000, 9999999999999999)
                print(f"The number of your card is {number}. Please remember it for future transactions.")
                count += 1
                f.write(str(count) + ". " + str(number) + " " + str(password) + "\n")
    elif x == '2':
        with open('atm.txt', 'r') as f:
            lines = f.readlines()
            number = input("Please enter the credit card number.\n")
            for index, line in enumerate(lines):
                if number in line:
                    password = input("Please enter the password.\n")
                    if password in line:
                        line_check = line.split(" ")
                        amount = input("How much money do you want to withdraw?\n")
                        if amount.isnumeric() and int(amount) > 0:
                            if int(line_check[3]) >= int(amount):
                                line_check_stripped = [x.strip() for x in line_check]
                                total = int(line_check_stripped[3]) - int(amount)
                                line_check_stripped[3] = str(total) + "\n"
                                edited_line = " ".join(line_check_stripped)
                                lines[index] = edited_line
                                with open('atm.txt', 'w') as f:
                                    for li in lines:
                                        f.write(li)
                                print(f"You have successfully cashed {amount} money out of your credit card! "
                                      f"Your new total is {total}.")
                                break
                            else:
                                print("You don't have enough money on the credit card to perform "
                                      "this operation.")
                                break
                        else:
                            print("You have entered incorrect value. Please try again!")
                            break
                    else:
                        print("You've entered incorrect password for this credit card. Please try again!")
                        break
                else:
                    print("You have entered incorrect credit card. Please try again.")
                    continue
    elif x == '3':
        with open('atm.txt', 'r') as f:
            lines = f.readlines()
            number = input("Please enter the credit card number.\n")
            for index, line in enumerate(lines):
                if number in line:
                    password = input("Please enter the password.\n")
                    if password in line:
                        line_check = line.split(" ")
                        amount = input("How much money do you want to put on your credit card?\n")
                        if amount.isnumeric() and int(amount) > 0:
                            try:
                                line_check_stripped = [x.strip() for x in line_check]
                                total = int(line_check_stripped[3]) + int(amount)
                                line_check_stripped[3] = str(total) + "\n"
                                edited_line = " ".join(line_check_stripped)
                                lines[index] = edited_line
                                with open('atm.txt', 'w') as f:
                                    for li in lines:
                                        f.write(li)
                                print(f"You have successfully put {amount} money to your credit card! "
                                      f"Your new total is {total}.")
                                break
                            except IndexError:
                                line_check_stripped = [x.strip() for x in line_check]
                                line_check_stripped.append(amount + "\n")
                                edited_line = " ".join(line_check_stripped)
                                lines[index] = edited_line
                                with open('atm.txt', 'w') as f:
                                    for li in lines:
                                        f.write(li)
                                print(f"You have successfully put {amount} money to your credit card! "
                                      f"Your new total is {amount}.")
                                break
                        else:
                            print("You have entered incorrect value. Please try again!")
                            break
                    else:
                        print("You've entered incorrect password for this credit card. Please try again!")
                        break
                else:
                    print("You have entered incorrect credit card. Please try again.")
                    continue
    elif x == '4':
        with open('atm.txt', 'r') as f:
            lines = f.readlines()
            number = input("Please enter the credit card number.\n")
            for line in lines:
                if number not in line:
                    print("You have entered incorrect credit card. Please try again.")
                    continue
                else:
                    password = input("Please enter the password.\n")
                    for l in lines:
                        if number in l:
                            line_check = l.split(" ")
                            line_check_stripped = [x.strip() for x in line_check]
                            if line_check_stripped[2] == password:
                                print(f"You have {line_check_stripped[3]} money on your credit card.")
                                break
                            else:
                                print("You've entered incorrect password for this credit card. Please try again!")
                                break
print('Bye!')