import random
import string

def generate_password(length, has_uppercase=True, has_lowercase=True, has_numbers=True, has_symbols=True):
    char_sets = []
    if has_uppercase:
        char_sets.append(string.ascii_uppercase)
    if has_lowercase:
        char_sets.append(string.ascii_lowercase)
    if has_numbers:
        char_sets.append(string.digits)
    if has_symbols:
        char_sets.append(string.punctuation)
    if len(char_sets) < 1:
        print("Password must include at least one character type (uppercase, lowercase, numbers, or symbols).")
        return None
    all_chars = ''.join(char_sets)
    password = ''.join(random.choices(all_chars, k=length))
    return password

def generate_multiple_passwords(count, length, has_uppercase=True, has_lowercase=True, has_numbers=True, has_symbols=True):
    passwords = []
    for _ in range(count):
        password = generate_password(length, has_uppercase, has_lowercase, has_numbers, has_symbols)
        if password:
            passwords.append(password)
    return passwords

def main():
    try:
        length = int(input("Enter desired password length: "))
        count = int(input("Enter the number of passwords to generate: "))
        if length <= 0 or count <= 0:
            print("Length and count must be positive integers.")
            return

        has_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        has_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        has_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        passwords = generate_multiple_passwords(count, length, has_uppercase, has_lowercase, has_numbers, has_symbols)
        if passwords:
            print("Generated passwords:")
            for password in passwords:
                print(password)
        else:
            print("No passwords generated.")
    except ValueError:
        print("Invalid input. Please enter valid integers for length and count.")

if __name__ == "__main__":
    main()
