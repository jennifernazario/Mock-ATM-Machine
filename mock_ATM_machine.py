from datetime import datetime
import random

# dictionary
database = {}  # dictionary


# Beginning of program
def main():
    # Greets user and displays the time.
    today = datetime.now()
    print("Today's date and time is", today)

    while True:
        initiate_system()


# Initiates system
def initiate_system():
    print("Welcome to Bank for Everyone")
    active_account = int(input("Do you have an account with us?: 1(yes) 2 (no) \n"))
    if active_account == 1:
        login()
    elif active_account == 2:
        register()
    else:
        print("Invalid response. Please try again.")
        initiate_system()


# Direct user to login with their account number AND password.
def login():
    print("****** Login ******")

    existing_account_number = int(input("\nWhat is your account number?\n"))
    password = input("What is your password? \n")

    for account_number, user_details in database.items():
        if account_number == existing_account_number:
            if user_details[3] == password:
                bank_operation(user_details)
    print("Invalid account number or password.")
    login()


# Direct user to register for a new account.
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
    print("Your account number is: " + str(account_number))
    print("Please store your account number in a secure place.")
    print("=============================")
    login()


def bank_operation(user):
    print("Welcome " + str(user[0]) + " " + str(user[1]))
    print("(1) Deposit")
    print("(2) Withdraw")
    print("(3) Logout")
    print("(4) Exit")
    selected_option = int(input("What would you like to do? \n"))
    current_balance = int(1500)
    if selected_option == 1:
        deposit_operation(current_balance)
    elif selected_option == 2:
        withdrawal_operation(current_balance)
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected")
    bank_operation(user)


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


# Clears all sessions.
def logout():
    login()


# Displays the 3 options available.
def display_options():
    print("Please type one of the available options:")
    print("1: Withdrawal")
    print("2: Cash Deposit")
    print("3: Complaint")


def deposit_operation(current_balance):
    deposit_amount = int(input("How much would you like to deposit? \n"))
    current_balance += deposit_amount
    print("Your current balance is " + str(current_balance) + ".")


def withdrawal_operation(current_balance):
    withdrawal_amount = int(input("How much would you like to withdraw? \n"))
    current_balance -= withdrawal_amount
    print("Take your cash!")
    print("Your current balance is " + str(current_balance) + ".")


if __name__ == "__main__":
    main()
