from tkinter import *
from tkinter import messagebox, filedialog
import random
import string

overall_font = "Righteous"
overall_font_size = "14"
overall_background_button = "#00008B"

pass_generator_file = Tk()
pass_generator_file.title("Password Generator")
pass_generator_file.config(width=600, height=400)  # Adjusted width for the frame and other content


# Create another frame for the password generator interface
frame_02 = Frame(pass_generator_file, width=450, height=250)
frame_02.grid(row=0, column=1)

# Add the password file generation widgets inside frame_02
password_lenghts = Label(frame_02, text="LENGTH", font=("Righteous", overall_font_size), fg=overall_background_button)
password_lenghts.place(x=10, y=10)

length_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
length_entry.insert(0, "9")
length_entry.place(x=200, y=10)

password_pieces = Label(frame_02, text="PASSES / FILE", font=("Righteous", overall_font_size), fg=overall_background_button)
password_pieces.place(x=10, y=40)

length_pieces_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
length_pieces_entry.insert(0, "10000")
length_pieces_entry.place(x=200, y=40)

password_pieces_sum = Label(frame_02, text="PASSES FILES", font=("Righteous", overall_font_size), fg=overall_background_button)
password_pieces_sum.place(x=10, y=70)

length_pieces_sum_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
length_pieces_sum_entry.insert(0, "1")
length_pieces_sum_entry.place(x=200, y=70)

special_chars = Label(frame_02, text="SPECIAL CHARS", font=("Righteous", overall_font_size), fg=overall_background_button)
special_chars.place(x=10, y=100)

special_chars_entry = Entry(frame_02, font=("Righteous", int(overall_font_size) - 2), fg=overall_background_button, justify='center', width=24)
special_chars_entry.insert(0, r"!§$%&/()=?+*#-_.:,;<>+-")
special_chars_entry.place(x=200, y=100)

file_names = Label(frame_02, text="FILENAMES", font=("Righteous", overall_font_size), fg=overall_background_button)
file_names.place(x=10, y=130)

file_names_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
file_names_entry.insert(0, "passwords")
file_names_entry.place(x=200, y=130)

file_names_path = Label(frame_02, text="SAVE PATH", font=("Righteous", overall_font_size), fg=overall_background_button)
file_names_path.place(x=10, y=160)

file_names_path_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
file_names_path_entry.insert(0, r"C:/Temp/")
file_names_path_entry.place(x=200, y=160)

def generate_password(length, special_chars):
    characters = string.ascii_letters + string.digits + special_chars
    return ''.join(random.choice(characters) for i in range(length))

def generate_and_save_passwords():
    length = int(length_entry.get())
    passes_per_file = int(length_pieces_entry.get())
    num_files = int(length_pieces_sum_entry.get())
    special_chars = special_chars_entry.get()
    file_name = file_names_entry.get()
    file_path = file_names_path_entry.get()
    passwords = set()  # to ensure uniqueness
    for _ in range(num_files):
        with open(f"{file_path}{file_name}_{_+1}.txt", "w") as f:
            for _ in range(passes_per_file):
                password = generate_password(length, special_chars)
                while password in passwords:  # ensure uniqueness
                    password = generate_password(length, special_chars)
                passwords.add(password)
                f.write(password + "\n")

generate_button = Button(frame_02,
                         text="GENERATE FILES",
                         font=("Righteous", overall_font_size),
                         fg=overall_background_button,
                         command=generate_and_save_passwords,
                         width=37)
generate_button.place(x=10, y=200)

pass_generator_file.mainloop()