PDF and Image to Base64 JSON Converter

This Python class provides a method to convert PDF files and image files (JPEG, PNG) into Base64-encoded strings, which are then organized into a JSON object. The purpose of this class is to facilitate the conversion of PDF documents and images for storage or transmission as Base64 strings.

Usage
Installation

Ensure you have Python installed on your system.
Install the required libraries using pip:
bash
Copy code
pip install PyMuPDF
Example Usage

python
Copy code
from converter import Converter

# Initialize Converter object
converter = Converter()

# Convert PDF file to JSON
pdf_file_path = "example.pdf"
pdf_json = converter.convert_to_json(pdf_file_path)
print(pdf_json)

# Convert image file to JSON
image_file_path = "example.png"
image_json = converter.convert_to_json(image_file_path)
print(image_json)
Replace "example.pdf" and "example.png" with the paths to your PDF and image files respectively.

Method: convert_to_json(file_path)
Parameters:
file_path (str or bytes): Path to the file or file content in bytes.
Returns:
A dictionary containing the conversion result.
message: Indicates whether the conversion was successful or failed.
data: Base64-encoded string(s) organized as JSON data.

Dependencies

PyMuPDF: Python library for PDF manipulation.
base64: Python module for Base64 encoding and decoding.
io: Python module for working with streams.
json: Python module for JSON serialization and deserialization.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to adjust or expand upon this README as needed for your project!