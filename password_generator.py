"""
Project 3 - Random Password Generator
Made by: Seemab Fatima
Batch 2026 - DecodeLabs Internship
"""

import secrets
import string

SYMBOLS = "!@#$%^&*()_+-="


def get_valid_length():
    # keep asking till we get a proper number
    while True:
        raw = input("How long should your password be? (min 6): ")
        if raw.isdigit() and int(raw) >= 6:
            return int(raw)
        print("Enter a valid number, at least 6.")


def get_yes_no(question):
    # keep asking until the user actually types y or n
    while True:
        ans = input(question + " (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please enter y or n.")


def build_character_pool(use_digits, use_symbols):
    pool = string.ascii_letters
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += SYMBOLS
    return pool


def make_password(length, use_digits, use_symbols):
    pool = build_character_pool(use_digits, use_symbols)

    # fill the password randomly first
    password_chars = [secrets.choice(pool) for _ in range(length)]

    # now make sure required character types are actually present
    required = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase)]
    if use_digits:
        required.append(secrets.choice(string.digits))
    if use_symbols:
        required.append(secrets.choice(SYMBOLS))

    # place each required character at a different random position
    # so we don't accidentally overwrite one required char with another
    positions = list(range(length))
    for char in required:
        pos = secrets.choice(positions)
        positions.remove(pos)
        password_chars[pos] = char

    return "".join(password_chars)


def rate_strength(length, use_digits, use_symbols):
    pool_size = 52  # letters only by default
    if use_digits:
        pool_size += 10
    if use_symbols:
        pool_size += 14

    combinations = pool_size ** length

    if combinations < 10 ** 12:
        return "Weak"
    elif combinations < 10 ** 18:
        return "Decent"
    elif combinations < 10 ** 30:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=" * 45)
    print("   PASSWORD GENERATOR - by Seemab Fatima")
    print("=" * 45)

    while True:
        length = get_valid_length()
        include_digits = get_yes_no("Include numbers?")
        include_symbols = get_yes_no("Include symbols?")

        # length has to be enough to fit all the required character types
        min_required = 2 + include_digits + include_symbols
        if length < min_required:
            print(f"Length too short to include everything you picked. Needs at least {min_required}.")
            continue

        password = make_password(length, include_digits, include_symbols)

        print("\nYour password:", password)
        print("Strength:", rate_strength(length, include_digits, include_symbols))

        if not get_yes_no("\nGenerate another one?"):
            print("\nDone. Stay safe!")
            break
        print()


if __name__ == "__main__":
    main()