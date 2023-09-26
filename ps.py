import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return

    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    character_pool = ""
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation

    if not character_pool:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create main window
root = tk.Tk()
root.title("Password Generator")
#root.maxsize(width=300,height=300)
#root.minsize(width=300,height=300)
root.geometry("600x600")
# Load the image
image_path = PhotoImage(file ='C:\\Users\\user\\Downloads\\ezgif.com-gif-maker (1).gif')
bg_image =tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)



# Create widgets
length_label = tk.Label(root, text="Password Length:",fg = "black",font=('Georgia',18))
length_entry = tk.Entry(root)

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", font=('Georgia',18),variable=lowercase_var)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase",font=('Georgia',18), variable=uppercase_var)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits",font=('Georgia',18), variable=digits_var)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", font=('Georgia',18),variable=special_chars_var)

generate_button = tk.Button(root, text="Generate Password",font=('Georgia',18), command=generate_password)
password_label = tk.Label(root, text="Generated Password: ",font=('Georgia',18))



# Place widgets using grid layout
length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry.grid(row=0, column=1,sticky="w", padx=10, pady=5)
lowercase_checkbox.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
uppercase_checkbox.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)
digits_checkbox.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)
special_chars_checkbox.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
#image_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)  # Place the image label






# Start GUI event loop
root.mainloop()
