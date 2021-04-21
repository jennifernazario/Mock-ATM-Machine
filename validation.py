def account_number_validation(account_number):
    # Check to see if the account number is not empty.
    # Check to see if the account number is 10 digits.
    # Check if the account number is an integer.

    # check if account number exists
    if account_number:
        # casting: converts account number into a string because we cannot check the length of an integer
        # if account number exists, checks data type, and then check if account number is 10 strings long
        try:
            # checks if datatype is accurate
            # casting: tries to convert account number string to integer
            int(account_number)
            if len(str(account_number)) == 10:
                # if we successfully convert the string to an integer, return true
                return True
        # if we are unable to convert into an integer, we catch the error
        except ValueError:
            return False
        except TypeError:
            return False
    return False

# def registration_input_validation():
# check if there is a list of inputs
# check each item in the list and make sure they are the correct data types
