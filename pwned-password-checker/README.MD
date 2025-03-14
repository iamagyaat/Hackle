# How It Works
Example Run:

Enter the directory containing breached password files: /path/to/passwords

Enter a password to check (or type 'exit' to quit): password123
🔴 The password 'password123' has been found in: /path/to/passwords/leaked.txt at line 42

Enter a password to check (or type 'exit' to quit): mysecurepass
🟢 The password 'mysecurepass' is safe or not found in the provided files.

Enter a password to check (or type 'exit' to quit): exit
Exiting the program.



# How to Run the Script

Save the script as check_password.py.
Run it from the terminal:

    python check_password.py


Enter your breached password directory.
Keep checking multiple passwords until you type "exit".