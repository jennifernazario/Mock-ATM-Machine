from datetime import datetime
import random
import validation
import database
from getpass import getpass


# Beginning of program
def main():
    # Welcomes the user and displays the current time.
    print("Welcome to Bank for Everyone")
    today = datetime.now()
    print("Today's date and time is", today)
    # Initiates system
    initiate_system()


# Initiates system by asking if a user has an account.
def initiate_system():
    active_account = int(input("Do you have an account with us?: 1(yes) 2 (no) \n"))
    # Directs the user to login to their existing account.
    if active_account == 1:
        login()
    # Directs the user to register for a new account.
    elif active_account == 2:
        register()
    # Directs the user to select an option again.
    else:
        print("Invalid response. Please try again.")
        # Initiates system by asking if a user has an account.
    initiate_system()


# Directs the user to login to their existing account.
def login():
    print("****** Login ******")
    # Direct user to login with their account number AND password.
    existing_account_number = input("\nWhat is your account number?\n")
    # is the account number valid?
    valid_account_number = validation.account_number_validation(existing_account_number)
    # if the account number is valid, proceed
    if valid_account_number:
        # asks for a password if the account number is valid
        password = getpass("What is your password? \n")

        user = database.authenticated_user(existing_account_number, password);

        if user:
            bank_operation(user, existing_account_number)

        print("Invalid account or number")

        # Directs the user to login to their existing account.
        login()
    else:
        print("Invalid account number. Check that you have exactly 10 integers")
        initiate_system()


# Directs the user to register for a new account
def register():
    print("****** Register for an account ******")
    # Directs the user to type their first name, last name, and email address.
    first_name = str(input("What is your first name? \n"))
    last_name = str(input("What is your last name? \n"))
    email_address = str(input("What is your email address? \n"))
    # Makes sure that the email address must contain at least an "@" character
    if set(email_address) >= {"@", "."}:
        pass
    else:
        print("Please type a real email address.")
        register()

    # Directs the user to create a password.
    password = getpass("Please create a password: \n")

    # Randomly generates an account number.
    account_number = generate_account_number()

    # account balance?
    account_balance = 1500

    is_user_created = database.create(account_number, first_name, last_name, email_address, password)

    # Prints confirmation upon the creation of a new account.
    if is_user_created:
        print("Your account has been created.")
        print("=============================")
        # Prints randomly generated account number.
        print("Your account number is: " + str(account_number))
        print("Please store your account number in a secure place.")
        print("=============================")
        # Directs the user to login to their existing account.
        login()
    else:
        print("Something went wrong, please try again")
        # help: not sure if needed
        register()


# This function allows users to deposit, withdraw, logout, or exit the program.
def bank_operation(user, account_number):
    print("Welcome " + str(user[0]) + " " + str(user[1]))
    selected_option = int(input("What would you like to do? \n(1) Deposit \n(2) Withdraw \n(3) Logout \n(4) Exit "
                                "\n"))
    current_balance = database[account_number][4]

    # Direct user to the deposit screen.
    if selected_option == 1:
        deposit_operation(current_balance, account_number)
    # Direct user to the withdrawal screen.
    elif selected_option == 2:
        withdrawal_operation(current_balance, account_number)
    # Direct user to the logout screen.
    elif selected_option == 3:
        logout()
    # Direct user to the exit screen.
    elif selected_option == 4:
        # Exits the program.
        exit()
    # Redirects user to the bank operation screen upon selecting an invalid option.
    else:
        print("Invalid option selected")
        bank_operation(user, account_number)


# Randomly generates an account number.
def generate_account_number():
    return random.randrange(1111111111, 9999999999)


# Direct user to the logout screen.
def logout():
    # Clears all sessions
    login()


# Displays the 3 options available.
def display_options():
    print("Please type one of the available options:")
    print("1: Withdrawal")
    print("2: Cash Deposit")
    print("3: Complaint")


# Direct user to the deposit screen.
def deposit_operation(current_balance, account_number):
    deposit_amount = int(input("How much would you like to deposit? \n"))
    current_balance += deposit_amount
    database[account_number][4] = current_balance
    print("Your current balance is " + str(current_balance) + ".")
    # return current_balance
    # I need help


# Direct user to the withdrawal screen.
def withdrawal_operation(current_balance, account_number):
    # asks user how much money they would like to withdraw
    withdrawal_amount = int(input("How much would you like to withdraw? \n"))
    # check if current balance is > withdrawal balance
    if current_balance > withdrawal_amount:
        pass
    else:
        print("You do not have enough money in your account. Please select a smaller amount to withdraw.")
        return withdrawal_operation(current_balance, account_number)
    # deduct withdrawn amount from current balance
    current_balance -= withdrawal_amount
    database[account_number][4] = current_balance
    print("Take your cash!")
    # Displays current balance
    print("Your current balance is " + str(current_balance) + ".")


if __name__ == "__main__":
    main()
