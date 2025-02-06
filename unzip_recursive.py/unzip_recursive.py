import os
import zipfile

def extract_zip(zip_path):
    """Extracts a zip file into a uniquely named folder to avoid conflicts."""
    base_folder = zip_path.replace('.zip', '')  # Folder name same as zip file
    extract_to = base_folder

    # Ensure extraction directory doesn't conflict with an existing file
    if os.path.isfile(extract_to):
        extract_to = base_folder + "_unzipped"

    os.makedirs(extract_to, exist_ok=True)  # Create directory if it doesn't exist

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)  # Extract files into this folder
        print(f"✅ Extracted: {zip_path} -> {extract_to}")
    except zipfile.BadZipFile:
        print(f"❌ Error: Bad zip file - {zip_path}")

def find_and_extract_zips(directory):
    """Finds and extracts all zip files in the given directory, maintaining structure."""
    extracted = True  # Flag to track ZIP extraction

    while extracted:
        extracted = False  # Reset flag before each pass
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".zip"):
                    zip_path = os.path.join(root, file)

                    # Ensure ZIP is not inside an already extracted folder
                    extract_folder = zip_path.replace('.zip', '')
                    if os.path.exists(extract_folder):
                        print(f"⚠️ Skipping already extracted: {zip_path}")
                        continue

                    extract_zip(zip_path)  # Extract into a named folder
                    os.remove(zip_path)  # Delete the zip file after extraction
                    print(f"🗑️ Deleted: {zip_path}")
                    extracted = True  # Continue checking for more zip files

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Recursively extract all zip files while preserving folder structure.")
    parser.add_argument("directory", type=str, help="Path to the directory containing zip files.")
    
    args = parser.parse_args()
    
    if os.path.exists(args.directory):
        find_and_extract_zips(args.directory)
        print("\n✅ All ZIP files extracted into respective folders and deleted.")
    else:
        print("❌ Error: Directory does not exist.")
