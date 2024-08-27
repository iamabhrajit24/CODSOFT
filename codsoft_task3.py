#task:PASSWORD GENERATOR
import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define the character set based on user preferences
    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def get_user_preferences():
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user preferences for password complexity
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    return length, use_uppercase, use_digits, use_special

def main():
    # Get user preferences
    length, use_uppercase, use_digits, use_special = get_user_preferences()

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special)

    # Display the generated password
    print(f"Generated Password: {password}")

# Run the password generator
main()
