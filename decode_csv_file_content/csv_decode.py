import csv
import os
import urllib.parse
import html

def decode_string(value):
    """Decodes both URL-encoded and HTML-encoded strings."""
    decoded_value = urllib.parse.unquote(value)  # URL decode
    decoded_value = html.unescape(decoded_value)  # HTML decode
    return decoded_value

def process_csv(file_path):
    """Reads a CSV file, decodes all encoded strings, and saves a new file with the decoded content."""
    output_file = file_path.replace('.csv', '_decoded.csv')  # Save as a new file

    changes = []  # Store cell-wise changes

    with open(file_path, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row_idx, row in enumerate(reader):
            new_row = []
            for col_idx, cell in enumerate(row):
                decoded_cell = decode_string(cell)
                new_row.append(decoded_cell)

                # Store only changed cells
                if cell != decoded_cell:
                    changes.append((row_idx + 1, col_idx + 1, cell, decoded_cell))

            writer.writerow(new_row)

    return output_file, changes

def main():
    file_path = input("Enter the CSV file name: ").strip()

    if not os.path.exists(file_path):
        print("❌ Error: The specified file does not exist.")
        return

    output_file, changes = process_csv(file_path)

    print(f"\n✅ Decoded CSV saved as: {output_file}")

    # Display changes in a table format
    if changes:
        print("\n🔍 Changes made (Row, Column, Original → Decoded):")
        print("-" * 80)
        for row, col, original, decoded in changes:
            print(f"Row {row}, Col {col}: '{original}' → '{decoded}'")
        print("-" * 80)
    else:
        print("✅ No encoded strings found. The file remains unchanged.")

if __name__ == "__main__":
    main()
