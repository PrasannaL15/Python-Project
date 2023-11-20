# Python-Test-Harness
Prasanna Limaye plimaye@stevens.edu

Github URL : https://github.com/PrasannaL15/Python-Project

Hours Spend on the project : 35



# Automated Testing with `test.py`

This repository includes an automated testing script, `test.py`, designed to validate various functionalities within the codebase in the directory prog/. The script is structured to test three primary components:

## Testing Components

### Word Count Functionality (`wc.py`)

The `wc.py` script provides word count functionality with different flags (`-l`, `-w`, `-c`). Test cases cover:

- Multiple input files.
- Flags usage (-l, -w, -c).
- Standard input usage.

### JSON Formatter (`gron.py`)

The `gron.py` script converts JSON data to grepable format. Test scenarios include:

- Various input JSON files covering variety of test cases.
- Standard input usage.
- Formatting flag to provide base object.

### Bulk Image Converter (`bic.py`)

The `bic.py` script handles bulk image conversions. Tests cover:

- Conversion of different image formats.

## Running Tests

To run the tests:

1. Ensure Python 3.x is installed.
2. Navigate to the project directory.
3. Use following command to install all the required libraries 
   ```
   pip install -r requirements.txt

   ``` 
3. Execute the `test.py` script:

   ```bash
   python test.py
