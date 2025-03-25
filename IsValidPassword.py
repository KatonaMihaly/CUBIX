def is_valid_password(s):
    lenght = True if len(s) >= 6 else False
    lowercase = any(char.islower() for char in s)
    uppercase = any(char.isupper() for char in s)
    number = any(char.isdigit() for char in s)
    special = any(not char.isalnum() for char in s)
    
    return lenght and lowercase and uppercase and number and special

input_str = input("Enter a password: ")
if is_valid_password(input_str):
    print("Valid password.")
else:
    print("Invalid password.")
    print("Must be at least 6 characters long.")
    print("Must contain at least one number.")
    print("Must contain at least one uppercase letter.")
    print("Must contain at least one special character.")
    print("Must contain at least one lowercase letter.")