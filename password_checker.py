import string #Import string module to access special characters

def check_password_strength(passowrd):
    if len(password) <8:
        return "Weak passwork: Must be at least 8 characters long"
    #Check for uppercase, lowercase, digits, and special characters
    has_upper =any(char.isupper()for char in password)
    has_lower =any(char.islower()for char in password)
    has_digit =any(char.isdigit()for char in password)
    has_special = any(char in string.punctuation for char in password)
    #check if all conditions are met
    if has_upper and has_lower and has_digit and has_special:
        return "Strong password!."
    else: 
        return "Weak password: Try using uppercase, lowercase, numbers, and special characters."
#Test it
password = input("Enter your password: ")
print(check_password_strength(password))


