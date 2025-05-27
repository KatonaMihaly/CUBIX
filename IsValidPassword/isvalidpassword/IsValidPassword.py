# RULESET ----------------------------------------------
import numpy as np

def interactive_input():
    """
    Prompt the user to enter a password interactively.

    Returns:
        str: The password entered by the user.
    """
    input_str = input("Enter your password: ")
    print(f"Received input: {input_str}")
    return input_str

def is_valid_length(s):
    """
    Check if the input string meets the minimum length requirement.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the string has at least 6 characters, False otherwise.
    """
    return True if len(s) >= 6 else False

def is_valid_lowercase(s):
    """
    Check if the input string contains at least one lowercase letter.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if at least one lowercase letter is present, False otherwise.
    """
    return any(char.islower() for char in s)

def is_valid_uppercase(s):
    """
    Check if the input string contains at least one uppercase letter.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if at least one uppercase letter is present, False otherwise.
    """
    return any(char.isupper() for char in s)

def is_valid_numeric(s):
    """
    Check if the input string contains at least one numeric digit.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if at least one digit is present, False otherwise.
    """
    return any(char.isdigit() for char in s)

def is_valid_special(s):
    """
    Check if the input string contains at least one special (non-alphanumeric) character.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if at least one special character is present, False otherwise.
    """
    return any(not char.isalnum() for char in s)

def is_valid_sum(s):
    """
    Check if the sum of all digits in the string equals 25.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the sum of digits is 25, False otherwise.
    """
    return sum([int(char) for char in s if char.isdigit()]) == 25

def is_valid_month(s):
    """
    Check if the input string contains the name of any month.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if any month name is present, False otherwise.
    """
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    return any(month in s.lower() for month in months)

def is_valid_root(s):
    """
    Check if the input string contains at least one digit whose square root is greater than 2.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if at least one digit has a square root greater than 2, False otherwise.
    """
    return any(np.sqrt(int(char)) > 2 for char in s if char.isdigit())

# def is_valid_rule(s):
#     """
#     Placeholder for additional rule validation.
#
#     Parameters:
#         s (str): The string to be checked.
#
#     Returns:
#         bool: True if the rule is satisfied, False otherwise.
#     """
#     return True

def validate_password(input_str):
    if not is_valid_length(input_str):
        return "Must be at least 6 characters long. Try again."
    elif not is_valid_lowercase(input_str):
        return "Must contain at least one lowercase letter. Try again."
    elif not is_valid_uppercase(input_str):
        return "Must contain at least one uppercase letter. Try again."
    elif not is_valid_numeric(input_str):
        return "Must contain at least one number. Try again."
    elif not is_valid_special(input_str):
        return "Must contain at least one special character. Try again."
    elif not is_valid_sum(input_str):
        return "The digits in the password must add up to 25. Try again."
    elif not is_valid_month(input_str):
        return "Must contain at least one month. Try again."
    elif not is_valid_root(input_str):
        return "Must contain a number which root is more than 2. Try again."
    # elif not is_valid_rule(input_str):
    #     return "Must contain ...")
    else:
        return None

def main():
    """
    Main function to interactively prompt the user for a password and validate it
    against a set of predefined rules. Prints feedback for each failed rule.
    """

    while True:
        input_str = input("Enter your password: ")
        error = validate_password(input_str)
        if error:
            print(error)
        else:
            print("You win!")
            break

if __name__ == '__main__':
    main()
