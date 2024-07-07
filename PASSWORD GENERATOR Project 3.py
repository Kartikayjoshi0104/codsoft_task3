import random
import string

def get_user_input():
    """Prompt the user to specify the desired length of the password."""
    while True:
        try:
            length = int(input("Enter the desired length of the password (must be at least 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length):
    """Generate a password using a combination of random characters of the specified length."""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def display_password(password):
    """Display the generated password on the screen."""
    print(f"Generated password: {password}")

def main():
    length = get_user_input()
    password = generate_password(length)
    display_password(password)

if __name__ == "__main__":
    main()
