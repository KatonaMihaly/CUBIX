# RULESET ----------------------------------------------
import numpy as np
import os

def interactive_input():
    input_str = input("Enter your password: ")
    print(f"Received input: {input_str}")
    return input_str

def is_valid_length(s):
    return True if len(s) >= 6 else False

def is_valid_lowercase(s):
    return any(char.islower() for char in s)

def is_valid_uppercase(s):
    return any(char.isupper() for char in s)

def is_valid_numeric(s):
    return any(char.isdigit() for char in s)

def is_valid_special(s):
    return any(not char.isalnum() for char in s)

def is_valid_sum(s):
    return sum([int(char) for char in s if char.isdigit()]) == 25

def is_valid_month(s):
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    return any(month in s.lower() for month in months)

def is_valid_root(s):
    return any(np.sqrt(int(char)) > 2 for char in s if char.isdigit())

# def is_valid_rule(s):
#     return True

# MAIN --------------------------------------------------
while True:

    if os.getenv('TEAMCITY_VERSION') is None:
        input_str = interactive_input()
    else:
        input_str = os.getenv('USER_INPUT')

    if not is_valid_length(input_str):
        print("Must be at least 6 characters long.")
    elif not is_valid_lowercase(input_str):
        print("Must contain at least one lowercase letter.")
    elif not is_valid_uppercase(input_str):
        print("Must contain at least one uppercase letter.")
    elif not is_valid_numeric(input_str):
        print("Must contain at least one number.")
    elif not is_valid_special(input_str):
        print("Must contain at least one special character.")
    elif not is_valid_sum(input_str):
        print("The digits in the password must add up to 25.")
    elif not is_valid_month(input_str):
        print("Must contain at least one month.")
    elif not is_valid_root(input_str):
        print("Must contain a number which root is more than 2.")
    # elif not is_valid_rule(input_str):
    #     print("Must contain ...")

    else:
        print("You win!")
        break