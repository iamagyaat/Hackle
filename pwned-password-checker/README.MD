
# Requirement 
Before run this script, you need to download the pwned password files from the following link:
```
https://github.com/HaveIBeenPwned/PwnedPasswordsDownloader
```

Otherwise, you can use the common password files from the following link:
```
https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
```

# How to Run the Script

Save the script as check_password.py.
Run it from the terminal:

    python check_password.py

Enter the directory containing breached password files: /path/to/passwords

Enter a password to check (or type 'exit' to quit): password123
🔴 The password 'password123' has been found in: /path/to/passwords/leaked.txt at line 42

Enter a password to check (or type 'exit' to quit): mysecurepass
🟢 The password 'mysecurepass' is safe or not found in the provided files.

Enter a password to check (or type 'exit' to quit): exit
Exiting the program.

Enter your breached password directory.
Keep checking multiple passwords until you type "exit".