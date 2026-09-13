password = input("Enter the password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

if len(password) >= 12:
    score += 1

# Check for uppercase letter
if any(i.isupper() for i in password):
    score += 1

# Check for lowercase letter
if any(i.islower() for i in password):
    score += 1

# Check for number
if any(i.isdigit() for i in password):
    score += 1

# Check for special character
if any(not i.isalnum() for i in password):
    score += 1

# Check common passwords
common_passwords = [
    "abc",
    "abcdefg",
    "abc123",
    "qwerty",
    "password",
    "123456",
    "12345678"
]

if password.lower() in common_passwords:
    score = 0
    print("Password is too common!")
else:
    # Display password strength
    if score >= 6:
        print("Password is Strong")
    elif score >= 4:
        print("Password is Medium")
    else:
        print("Password is Weak")

print("Security Score:", score, "/ 6")