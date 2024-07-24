import os
from bs4 import BeautifulSoup

# Define the input and output directories
input_dir = 'D:/Files/salesforce-lightning-design-system-icons/utility'
output_dir = 'D:/Files/salesforce-lightning-design-system-icons/utility/output'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.svg'):
        # Construct full file path
        filepath = os.path.join(input_dir, filename)

        # Open and read the SVG file
        with open(filepath, 'r', encoding='utf-8') as file:
            svg_content = file.read()

        # Parse the SVG content with BeautifulSoup
        soup = BeautifulSoup(svg_content, 'xml')

        # Find the <svg> tag
        svg_tag = soup.find('svg')
        if svg_tag is not None:
            # Set the id attribute to the filename without the extension
            svg_tag['id'] = os.path.splitext(filename)[0]

            # Write the modified SVG content to the output directory
            output_filepath = os.path.join(output_dir, filename)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(str(soup))

print("SVG files processed and saved to the 'output' folder.")
