import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) < 6:
        remarks = "Weak: Password too short!"
        return strength, remarks

    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 1:
        remarks = "Weak password 😕"
    elif strength == 2:
        remarks = "Moderate password 🙂"
    elif strength == 3:
        remarks = "Strong password 💪"
    elif strength == 4:
        remarks = "Very strong password 🔥"

    return strength, remarks


password = input("Enter your password: ")
strength, remarks = check_password_strength(password)
print(f"Password strength: {strength}/4 → {remarks}")
