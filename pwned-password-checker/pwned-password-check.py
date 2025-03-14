#!/usr/bin/env python3 

import os

"""
Before run this script, you need to download the pwned password files from the following link:
https://github.com/HaveIBeenPwned/PwnedPasswordsDownloader
"""

def check_password_in_file(file_path, password):
    """
    Check if the password is in the specified file.
    Returns the line number if the password is found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if line.strip() == password:
                    return line_number
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return None

def find_password_in_directory(directory, password):
    """
    Search through all text files in the specified directory for the given password.
    If found, returns the file path and line number.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            line_number = check_password_in_file(file_path, password)
            
            if line_number is not None:
                return file_path, line_number
    
    return None, None

def main():
    directory = input("Enter the directory containing breached password files: ")
    password = input("Enter the password to check: ")

    file_path, line_number = find_password_in_directory(directory, password)

    if file_path and line_number:
        print(f"The password '{password}' has been found in: {file_path} at line {line_number}")
    else:
        print("This password is safe or not found in the provided files.")

if __name__ == "__main__":
    main()
