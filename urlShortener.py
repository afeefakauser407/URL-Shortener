import tkinter as tk
import pyshorteners
from tkinter import *

# Create the root window
root = Tk()
root.geometry("500x300")
root.configure(bg="lightblue")

# Function for URL shortening
def shortener():
    url = entry.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url)
    entry1.delete(0, END)
    entry1.insert(END, url_short)

# Label for entering the URL
Label(root, text="Enter the URL", font="arial 20 bold", bg="lightblue", fg="white").pack(fill='x')

# Entry box for URL input
entry = Entry(root, font="arial 14 ", bg="white", fg="lightblue", bd=3, width=40)
entry.pack(pady=20)

# Button to trigger the URL shortening function
Button(root, text="Submit", font="arial 12 bold", bg="white", fg="lightblue", bd=3, command=shortener).pack()

# Entry for displaying the shortened URL
entry1 = Entry(root, font="arial 20 ", bg="lightblue", fg="white", width=40)
entry1.pack(pady=20)

# Start the main loop
mainloop()
