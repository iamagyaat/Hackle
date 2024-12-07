#!/usr/bin/env python3

import os
import time
from collections import defaultdict

def rename_files_by_creation_date(directory):
    # Create a dictionary to keep track of the number of files for each date
    date_count = defaultdict(int)

    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Ensure it's a file, not a directory
        if os.path.isfile(file_path):
            # Get file creation time
            creation_time = os.path.getctime(file_path)
            creation_date = time.strftime('%Y%m%d', time.localtime(creation_time))

            # Increment the count for this date 
            date_count[creation_date] += 1

            # Create new file name in the format YYYYMMDD-1/2/3...
            new_filename = f"{creation_date}-{date_count[creation_date]}{os.path.splitext(filename)[1]}"

            # Create the new file path 
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file 
            print(f"Renaming {file_path} to {new_file_path}")
            os.rename(file_path, new_file_path)

if __name__ == "__main__":
    import argparse

    # Argument parser for directory input
    parser = argparse.ArgumentParser(description="Rename files by their creation date in format YYYYMMDD-1/2/3.")
    parser.add_argument("directory", type=str, help="The directory where files are located.")
    
    args = parser.parse_args()

    # Rename files in the given directory
    rename_files_by_creation_date(args.directory)
