from datetime import datetime
import random

# dictionary
database = {}  # dictionary


# Initiates system
def initiate_system():
    valid_option = False
    print("Welcome to Bank for Everyone")
    while not valid_option:
        active_account = int(input("Do you have an account with us?: 1(yes) 2 (no) \n"))
        if active_account == 1:
            valid_option = True
            login()
        elif active_account == 2:
            valid_option = True
            register()
        else:
            print("Invalid response. Please try again.")


# Direct user to login with their account number AND password.
def login():
    bank_operation()

    # str(input("What is your account number? \n"))
    # str(input("What is your password? \n"))


def register():
    print("****** Register for an account ******")
    first_name = str(input("What is your first name? \n"))
    last_name = str(input("What is your last name? \n"))
    email_address = str(input("What is your email address? \n"))
    password = str(input("Please create a password: \n"))

    account_number = generate_account_number()
    database[account_number] = [first_name, last_name, email_address, password]
    print("Your account has been created.")
    print("=============================")
    print("Your account number is " + str(account_number))
    print("Please store your account number in a secure place.")

    print("=============================")
    login()


def bank_operation():
    print("****** Login ******")


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


# Greets user and displays the time.
today = datetime.now()
print("Thank you for using the ATM today.")
print("Today's date and time is", today)


# Displays the 3 options available.
def display_options():
    print("Please type one of the available options:")
    print("1: Withdrawal")
    print("2: Cash Deposit")
    print("3: Complaint")


# Beginning of program
def main():
    initiate_system()
    while True:
        name = input("\nWhat is your name? \n")
        allowed_users = ["Jennifer", "Jenn", "Jen"]
        allowed_password = ["Password", "Pass", "Pas"]
        current_balance = int(1500)

        while name in allowed_users:
            password = input("What is your password? \n")
            user_id = allowed_users.index(name)
            if password != allowed_password[user_id]:
                print("Password is incorrect. Please try again.")

            else:
                display_options()
                while True:
                    try:
                        selected_option = int(input("Please select an option:\n"))
                        if selected_option == 1:
                            print("You have selected " + str(selected_option))
                            # After I ask how much someone would like to withdraw and they enter a number more than
                            # 2 times,it takes them back to the options instead of how much they would like to withdraw
                            # option.
                            withdrawal_amount = int(input("How much would you like to withdraw? \n"))
                            print("Take your cash!")
                            current_balance -= withdrawal_amount
                            print("Your current balance is " + str(current_balance) + ".")
                        elif selected_option == 2:
                            print("You have selected " + str(selected_option))
                            deposit_amount = int(input("How much would you like to deposit? \n"))
                            current_balance += deposit_amount
                            print("Your current balance is " + str(current_balance) + ".")
                        elif selected_option == 3:
                            print("You have selected " + str(selected_option))
                            str(input("What issue will you like to report? \n"))
                            print("Thank you for contacting us.")
                        else:
                            print("Invalid response. Please try again.")
                        display_options()
                    except ValueError:
                        print("Invalid response. Please try again.")

        else:
            print("Name not found. Please try again.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
