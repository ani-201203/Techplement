import string
import random

def generate_password(length, include_upper, include_lower, include_digits, include_special):
    character_list = ""
    if include_upper:
        character_list += string.ascii_uppercase
    if include_lower:
        character_list += string.ascii_lowercase
    if include_digits:
        character_list += string.digits
    if include_special:
        character_list += string.punctuation

    if not character_list:
        raise ValueError("At least one character set must be selected")

    # Ensure password contains at least one character from each selected set
    password = []
    if include_upper:
        password.append(random.choice(string.ascii_uppercase))
    if include_lower:
        password.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from the combined character list
    while len(password) < length:
        password.append(random.choice(character_list))

    # Shuffle the password list to avoid predictable sequences
    random.shuffle(password)
    
    return ''.join(password)

def main():
    # Getting password length
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number for password length.")
        return

    if length < 1:
        print("Password length must be at least 1.")
        return

    print('''Choose character set for password from these : 
            1. Uppercase Letters
            2. Lowercase Letters
            3. Digits
            4. Special characters
            5. Exit''')

    include_upper = include_lower = include_digits = include_special = False

    # Getting character set for password
    while True:
        choice = input("Pick a number (1-4) or 5 to finish: ")
        if choice == '1':
            include_upper = True
        elif choice == '2':
            include_lower = True
        elif choice == '3':
            include_digits = True
        elif choice == '4':
            include_special = True
        elif choice == '5':
            break
        else:
            print("Please pick a valid option!")

    try:
        password = generate_password(length, include_upper, include_lower, include_digits, include_special)
        print("Your password is:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


# Output:
# Enter password length: 10
# Choose character set for password from these :
#             1. Uppercase Letters
#             2. Lowercase Letters
#             3. Digits
#             4. Special characters
#             5. Exit
# Pick a number (1-4) or 5 to finish: 1
# Pick a number (1-4) or 5 to finish: 3
# Pick a number (1-4) or 5 to finish: 5
# Your password is: 4X9F5E9P6Y

# Enter password length: 5
# Choose character set for password from these :
#             1. Uppercase Letters
#             2. Lowercase Letters
#             3. Digits
#             4. Special characters
#             5. Exit
# Pick a number (1-4) or 5 to finish: 2
# Pick a number (1-4) or 5 to finish: 3
# Pick a number (1-4) or 5 to finish: 5
# Your password is: 2z9b3
