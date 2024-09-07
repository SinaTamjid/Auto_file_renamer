import os
import re
from pathlib import Path

# Path to the directory containing the images
data_dir = r"C:\Users\Lion\Desktop\images\char-5-epoch-6\train"
# Path to the directory where renamed images will be saved
output_dir = r"C:\Users\Lion\Desktop\images\renamed"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get list of all the images
images = sorted(list(map(str, list(Path(data_dir).glob("*.png")))))

# Regular expression to match the first 5 digits followed by any characters
pattern = re.compile(r"^\d{5}")

for image in images:
    # Get the file name
    file_name = os.path.basename(image)
    print(f"Processing file: {file_name}")  # Debugging statement
    # Find the first 5 digits at the beginning of the file name
    match = pattern.match(file_name)
    if match:
        # Get the number
        number = match.group(0)
        # Create the new file name
        new_file_name = f"{number}.png"
        new_file_path = os.path.join(output_dir, new_file_name)
        
        # Check if the new file name already exists
        if os.path.exists(new_file_path):
            print(f"File with name {new_file_name} already exists. Skipping rename.")  # Debugging statement
            continue  # Skip renaming if the file already exists
        
        # Rename the file
        os.rename(image, new_file_path)
        print(f"Renamed {file_name} to {new_file_name}")  # Debugging statement
    else:
        print(f"No match found for {file_name}")  # Debugging statement

print("Renaming completed.")
