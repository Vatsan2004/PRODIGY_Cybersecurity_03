import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`|\\-]', password)

    # Assess strength
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Provide feedback
    if strength == 5:
        feedback = "Excellent"
    elif strength == 4:
        feedback = "Good"
    elif strength == 3:
        feedback = "Fair"
    elif strength == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    return {
        "Password": password,
        "Length Criteria": length_criteria,
        "Uppercase Letters": bool(uppercase_criteria),
        "Lowercase Letters": bool(lowercase_criteria),
        "Numbers": bool(number_criteria),
        "Special Characters": bool(special_char_criteria),
        "Strength": feedback
    }

# Example usage:
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)

# Print results
print("\nPassword Strength Report:")
for key, value in result.items():
    print(f"{key}: {value}")
