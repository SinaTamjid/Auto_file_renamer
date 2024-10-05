import os
import re
from pathlib import Path

# Path to the directory containing the files
data_dir = r"your input folder that contains the files"
# Path to the directory where renamed files will be saved
output_dir = r"your output directory folder"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get list of all the images
images = sorted(list(map(str, list(Path(data_dir).glob("*.png")))))

# Regular expression to match the pattern name you wanna recognize or change
pattern = re.compile(r"??????")

for image in images:
    # Get the file name
    file_name = os.path.basename(image)
    print(f"Processing file: {file_name}")  # Debugging statement
    # Find the pattern from regular expression
    match = pattern.match(file_name)
    if match:
        # Get the match
        number = match.group(0)
        # Create the new file name
        # its could be number letters or anything you want
        new_file_name = f"{number}.with the format you want"
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
