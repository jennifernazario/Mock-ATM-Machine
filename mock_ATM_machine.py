from datetime import datetime
import random

# dictionary
database = {}  # dictionary


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
    existing_account_number = int(input("\nWhat is your account number?\n"))
    password = input("What is your password? \n")

    for account_number, user_details in database.items():
        if account_number == existing_account_number:
            if user_details[3] == password:
                bank_operation(user_details, account_number)
    print("Invalid account number or password.")
    # Directs the user to login to their existing account.
    login()


# Directs the user to register for a new account
def register():
    print("****** Register for an account ******")
    # Directs the user to type their first name, last name, and email address.
    first_name = str(input("What is your first name? \n"))
    last_name = str(input("What is your last name? \n"))
    email_address = str(input("What is your email address? \n"))
    # Directs the user to create a password.
    password = str(input("Please create a password: \n"))
    # Randomly generates an account number.
    account_number = generate_account_number()
    account_balance = 1500
    database[account_number] = [first_name, last_name, email_address, password, account_balance]

    # Prints confirmation of the creation of a new account.
    print("Your account has been created.")
    print("=============================")
    # Prints randomly generated account number.
    print("Your account number is: " + str(account_number))
    print("Please store your account number in a secure place.")
    print("=============================")
    # Directs the user to login to their existing account.
    login()


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


# Direct user to the withdrawal screen.
def withdrawal_operation(current_balance, account_number):
    withdrawal_amount = int(input("How much would you like to withdraw? \n"))
    current_balance -= withdrawal_amount
    database[account_number][4] = current_balance
    print("Take your cash!")
    print("Your current balance is " + str(current_balance) + ".")


if __name__ == "__main__":
    main()
