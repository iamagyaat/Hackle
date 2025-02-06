unzip_recursive


It's a Python program that recursively extracts all .zip files inside a given directory, including subfolders. It will continue extracting nested .zip files until no more are left. Finally, it will delete all .zip files and keep the extracted files and folders.

Steps:

    1. Extract all .zip files inside the given directory.
    2. Recursively check for nested .zip files and extract them.
    3. Continue the process until all .zip files are extracted.
    4. Delete all .zip files after extraction.

Command-line Usage:
Save the script as unzip_recursive.py.
Run it in the terminal with:

python unzip_recursive.py /path/to/directory
