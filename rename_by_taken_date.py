#!/usr/bin/env python3

import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime

def get_taken_date(image_path):
    """
    Extracts the date and time the photo was taken from the Exif metadata.
    """
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            return None
        
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            if decoded == 'DateTimeOriginal':
                return value  # Format: "YYYY:MM:DD HH:MM:SS" 
        
        return None
    except Exception as e:
        print(f"Error getting Exif data from {image_path}: {e}")
        return None

def format_date(date_str):
    """
    Converts the date from "YYYY:MM:DD HH:MM:SS" to "YYYYMMDD".
    """
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
        return date_obj.strftime('%Y%m%d')
    except ValueError:
        return None

def rename_jpg_files(directory):
    """
    Renames all .jpg/.JPG files in the specified directory based on the taken date.
    """
    file_counter = {}
    
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            file_path = os.path.join(directory, filename)
            
            # Extract the taken date from the image
            taken_date = get_taken_date(file_path)
            if taken_date:
                formatted_date = format_date(taken_date)
                
                if formatted_date:
                    # Handle multiple files taken on the same day
                    if formatted_date not in file_counter:
                        file_counter[formatted_date] = 1
                    else:
                        file_counter[formatted_date] += 1
                    
                    new_filename = f"{formatted_date}-{file_counter[formatted_date]}.jpg"
                    new_file_path = os.path.join(directory, new_filename)
                    
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                else:
                    print(f"Could not format date for {filename}")
            else:
                print(f"Exif date not found for {filename}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rename JPG files based on the date taken.")
    parser.add_argument("directory", help="Directory containing JPG files to rename.")
    args = parser.parse_args()

    rename_jpg_files(args.directory)
