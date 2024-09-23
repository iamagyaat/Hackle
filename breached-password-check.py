#!/usr/bin/env python3

import os

def load_breached_passwords(directory):
    """
    Load all breached passwords from text files in the specified directory.
    """
    breached_passwords = set()
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        breached_passwords.add(line.strip())
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return breached_passwords

def check_password(password, breached_passwords):
    """
    Check if the password is in the list of breached passwords.
    """
    return password in breached_passwords

def main():
    directory = input("Enter the directory containing breached password files: ")
    password = input("Enter the password to check: ")

    breached_passwords = load_breached_passwords(directory)

    if check_password(password, breached_passwords):
        print("This password has been breached!")
    else:
        print("This password is safe.")

if __name__ == "__main__":
    main()
