# ============================================
# Password Generator
# Author: Muhammad Sohaib Imran
# FAST-NUCES, Lahore | FinTech
# ============================================

import random
import string
import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print app header."""
    print("\n" + "=" * 45)
    print("          🔐 PASSWORD GENERATOR")
    print("          Muhammad Sohaib Imran")
    print("          FAST-NUCES, Lahore")
    print("=" * 45)


def check_strength(password):
    """Check and return password strength."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score <= 3:
        strength = "🔴 Weak"
    elif score <= 5:
        strength = "🟡 Medium"
    elif score <= 6:
        strength = "🟢 Strong"
    else:
        strength = "💪 Very Strong"

    return strength, feedback


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a random password based on user preferences."""
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest randomly
    remaining = length - len(password)
    password += random.choices(characters, k=remaining)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)


def get_yes_no(prompt):
    """Get a yes/no answer from user."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("  ❌ Please enter yes or no.")


def get_length():
    """Get desired password length from user."""
    while True:
        try:
            length = int(input("\n  🔢 Password length (8-64): "))
            if 8 <= length <= 64:
                return length
            else:
                print("  ❌ Length must be between 8 and 64.")
        except ValueError:
            print("  ❌ Please enter a valid number.")


def get_count():
    """Get number of passwords to generate."""
    while True:
        try:
            count = int(input("\n  🔢 How many passwords to generate? (1-10): "))
            if 1 <= count <= 10:
                return count
            else:
                print("  ❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("  ❌ Please enter a valid number.")


def main():
    """Main program loop."""
    clear_screen()
    print_header()
    print("\n  Welcome! Let's generate secure passwords.\n")

    while True:
        print("\n" + "-" * 45)
        print("  ⚙️  SETTINGS")
        print("-" * 45)

        # Get preferences
        length = get_length()

        print("\n  Select character types (yes/no):")
        use_upper   = get_yes_no("  Include UPPERCASE letters? (y/n): ")
        use_lower   = get_yes_no("  Include lowercase letters? (y/n): ")
        use_digits  = get_yes_no("  Include numbers (0-9)? (y/n): ")
        use_symbols = get_yes_no("  Include symbols (!@#$...)? (y/n): ")

        if not any([use_upper, use_lower, use_digits, use_symbols]):
            print("\n  ❌ You must select at least one character type!")
            continue

        count = get_count()

        # Generate passwords
        print("\n" + "-" * 45)
        print("  🔐 GENERATED PASSWORDS")
        print("-" * 45)

        for i in range(1, count + 1):
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            if password:
                strength, feedback = check_strength(password)
                print(f"\n  [{i}] {password}")
                print(f"      Strength: {strength}")
                if feedback:
                    print(f"      💡 Tip: {feedback[0]}")

        print("\n" + "-" * 45)

        # Generate more or quit
        again = get_yes_no("\n  🔄 Generate more passwords? (y/n): ")
        if not again:
            print("\n  Stay secure! 🔐")
            print("  — Muhammad Sohaib Imran | FAST-NUCES\n")
            break

        clear_screen()
        print_header()


if __name__ == "__main__":
    main()
