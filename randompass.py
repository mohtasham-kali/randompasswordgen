from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint

# Main window

root = Tk()
root.title("Random Password Generator Tool")
root.config(bg="black")
root.geometry("1000x600")

# Logo
logo = Label(root, text="Random", font=("Helvetica", 24, 'bold'), fg="white", bg="black")
logo.place(x=25,y=15)

# Title
title = Label(root, text="Welcome To Random", font=("Helvetica", 16, 'bold'), fg="white", bg="black")
title.pack(pady=25)

# Version
version = Label(root, text="Version: 1.0.0", font=("Helvetica", 10, 'bold'), fg="white", bg="black")
version.place(x=30, y=575)

# Border
color_border = Frame(root, width=800, height=500, bg="blue")
canvas = Canvas(color_border)
color_border.pack()

# Tabs
my_notebook = ttk.Notebook(color_border)
my_notebook.pack(pady=5,padx=5)

container = Frame(my_notebook)
container.pack(fill=BOTH, expand=True)

my_notebook.add(container, text="Password Generator Tool")

# Scrollable canvas
canvas = Canvas(container, width=850, height=450)
scroll = Scrollbar(container, command=canvas.yview)
canvas.config(yscrollcommand=scroll.set, scrollregion=(0,0,100,750), bg="gray22")
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)
frame = Frame(canvas, width=1450, height=1000, bg="gray22")
canvas.create_window(430,250, window=frame)
frame_1 = Frame(frame, width=798, height=305, bg="gray22")
frame_1.pack(pady=20)

# Title for generator
title_gen = Label(frame_1, text="Welcome to the generator", font=("Helvetica", 20, 'bold'), fg="white", bg="gray22")
title_gen.pack(pady=20)

my_password = chr(randint(33,126))

def new_random():
	if my_entry.get() == (""):
		error = Label(frame_1, text="Error: You must enter a number ...", font=("Helvetica", 8, 'bold'), bg="gray22", fg="red")
		error.pack()
		error.after(3000, error.destroy)

	else:

		# Clear box
		pw_entry.delete(0, END)

		# Get password length and convert to integer
		pw_length = int(my_entry.get())

		# Create a var to hold pass
		my_password = ''

		# Loop through password length
		for x in range(pw_length):
			my_password += chr(randint(33,126))

		# Output the password to the screen
		pw_entry.insert(0, my_password)

		# Print successfull
		succ = Label(frame_1, text="Successfully generated strong password", font=("Helvetica", 8, 'bold'), bg="gray22", fg="green")
		succ.pack()
		succ.after(3000, succ.destroy)
		my_entry.delete(0, END)


def clipboard():
	# Clear clipboard
	frame_1.clipboard_clear()
	# Copy to clipboard
	frame_1.clipboard_append(pw_entry.get())

	clipboard = Label(frame_1, text="Successfully copied to clipboard", font=("Helvetica", 8, 'bold'), bg="gray22", fg="green")
	clipboard.pack()
	clipboard.after(3000, clipboard.destroy)

# Frame
lf = LabelFrame(frame_1, text="How many characters would you like?", font=("Helvetica", 8, 'bold'), bg="gray22", fg="white")
lf.pack(pady=20)

# Craete the entry box for number of chars
my_entry = Entry(lf, font=("Helvetica", 24), bg="gray22", fg="white", borderwidth=2)
my_entry.pack(pady=20, padx=20)

# Create entry box for returned password
pw_entry = Entry(frame_1, text="",  font=("Helvetica", 24), bg="gray22", fg="white", borderwidth=0)
pw_entry.pack(pady=40)

# Buttons

my_button = Button(frame_1, text="Generate Strong Password", command = new_random, bg="gray22", fg="white", activebackground="darkblue", borderwidth=0)
my_button.place(x=50, y=225)

clip_button = Button(frame_1, text="Copy To Clipboard", command = clipboard, bg="gray22", fg="white", activebackground="darkblue", borderwidth=0)
clip_button.place(x=250, y=225)


root.mainloop()