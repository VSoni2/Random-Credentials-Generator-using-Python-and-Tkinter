import random
import string
import tkinter as tk

# Function to generate a random username
def generate_username(length=8):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate random credentials and update the result label
def generate_random_credentials():
    username = generate_username()
    password = generate_password()
    result_label.config(text="Random Username: " + username + "\nRandom Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Random Credentials Generator")

# Create a label for the title
title_label = tk.Label(window, text="Random Username and Password Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create a frame for the result label and button
frame = tk.Frame(window)
frame.pack(pady=10)

# Create a label to display the generated username and password
result_label = tk.Label(frame, text="", font=("Helvetica", 12))
result_label.pack(padx=20, pady=10)

# Create a button to generate random credentials
generate_button = tk.Button(frame, text="Generate Credentials", command=generate_random_credentials)
generate_button.pack()

# Start the GUI event loop
window.mainloop()
