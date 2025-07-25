import re
def password_strength(password):
# Check if the password contains at least one uppercase letter
    uppercase_regex = re.compile(r'[A-Z]')
    has_uppercase = bool(uppercase_regex.search(password))
# Check if the password contains at least one lowercase letter
    lowercase_regex = re.compile(r'[a-z]')
    has_lowercase = bool(lowercase_regex.search(password))
# Check if the password contains at least one digit
    digit_regex = re.compile(r'\d')
    has_digit = bool(digit_regex.search(password))
# Check if the password contains at least one special character
    special_char_regex = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    has_special_char = bool(special_char_regex.search(password))
# Check if the password meets all the criteria
    if has_uppercase and has_lowercase and has_digit and has_special_char and len(password)> 12:
        return "Strong"
    elif has_uppercase and has_lowercase and has_digit and len(password)> 8:
        return "Moderate"
    elif has_uppercase and has_lowercase or has_digit:
        return "Weak"
    else:
        return "Invalid Password"
# Example usage
password = input("Enter your password:")
strength = password_strength(password)
print("Password strength:", strength)
