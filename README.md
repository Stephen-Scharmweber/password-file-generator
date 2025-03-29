# Password Generator

A simple GUI-based password generator application built with Python and Tkinter. This tool allows you to generate large quantities of unique random passwords and save them to text files.

## Features

- Generate customizable length passwords
- Specify special characters to include
- Create multiple password files at once
- Set the number of passwords per file
- Choose output directory and filename prefix
- Ensures all generated passwords are unique

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)

## Usage

1. Run the script: `python password_generator.py`
2. Fill in the parameters:
   - **LENGTH**: Password length (default: 9)
   - **PASSES / FILE**: Number of passwords per file (default: 10,000)
   - **PASSES FILES**: Number of files to generate (default: 1)
   - **SPECIAL CHARS**: Special characters to include (default: `!§$%&/()=?+*#-_.:,;<>+-`)
   - **FILENAMES**: Base filename (default: "passwords")
   - **SAVE PATH**: Directory to save files (default: `C:/Temp/`)
3. Click "GENERATE FILES" button

## Output

The program will generate text files with the specified number of unique passwords each. Files will be named with your chosen prefix followed by a number (e.g., `passwords_1.txt`, `passwords_2.txt`, etc.).

## Customization

You can easily modify the default values in the code by changing the `.insert()` methods for each Entry widget.

## License

This project is open-source and free to use.
