# create record
# update record
# read record
# delete record
# CURD

# find user

# allows us to delete a file
import os
import validation

user_db_path = "data/user_record/"


def create(user_account_number, first_name, last_name, email_address, password):
    # create a file
    # name of the file will be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then delete created file

    user_data = first_name + "," + last_name + "," + email_address + "," + password + "," + str(0)

    if account_number_exists(user_account_number):
        return False

    if email_exists(email_address):
        print("user already exists")
        return False

    completion_state = False
    try:
        # if file is created,
        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        file_contains_data = read(user_db_path + str(user_account_number) + ".txt")
        if not file_contains_data:
            delete(user_account_number)

        delete(user_account_number)
    else:
        # if the file is created and there are no errors, add the user details to the file
        f.write(str(user_data));
        completion_state = True

    # always runs
    finally:
        f.close();
        return completion_state


def read(user_account_number):
    # find user with account number
    # fetch content of the file
    valid_account_number = validation.account_number_validation(user_account_number)
    try:
        # if it is a string
        if valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        # if it is an integer
        else:
            f = open(user_db_path + user_account_number, "r")
    except FileNotFoundError:
        # help
        print("user not found")
    except FileExistsError:
        print("user does not exist")
    except TypeError:
        print("Invalid account number format")
    else:
        # if there are no errors, read the file and send back to the user
        return f.readline()
    return False


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(user_account_number):
    # if the user exists, delete user account from the database
    # find user with account number
    # delete the user record (file)
    # return true
    successfully_deleted = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            successfully_deleted = True
        except FileNotFoundError:
            print("User not found.")

        finally:
            return successfully_deleted


# finds user based on account number
def email_exists(email):
    # lists every user in the database
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user), ",")
        if email in user_list:
            return True
    return False


def account_number_exists(account_number):
    # lists every user in the database
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def authenticated_user(account_number, password):
    if account_number_exists(account_number):
        user = str.split(read(account_number), ",")
        if password == user[3]:
            return user

    return False


print(account_number_exists(9054003195))


# print(email_exists("jennifernazario@gmail.com"))


# print(read({'one': 'two'}))
