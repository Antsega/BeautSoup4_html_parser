# Import the modules
import os
from bs4 import BeautifulSoup

# Define the source and destination folders
source_folder = "raw"
destination_folder = "parsed"

# Loop through the files in the source folder
for file in os.listdir(source_folder):
    # Check if the file is an html file
    if file.endswith(".html"):
        # Open the file and read its content
        with open(os.path.join(source_folder, file), "r", encoding="utf-8") as f:
            content = f.read()
        # Create a BeautifulSoup object from the content
        soup = BeautifulSoup(content, "html.parser")
        # Find all the elements that have an href attribute that contains the string "Skip to main content"
        elements = soup.find_all(class_="visually-hidden focusable skip-link")
        # Loop through the elements and remove them from the soup
        for element in elements:
            element.decompose()
        # Write the modified content to a new file in the destination folder
        with open(os.path.join(destination_folder, file), "w") as f:
            f.write(str(soup))
