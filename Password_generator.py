import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 1:
        return "Password length must be at least 1."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated password: {password}")

        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    password_generator()

    
