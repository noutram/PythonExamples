import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Hello", "Hello World")

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Hello World App")
root.geometry("400x300")  # Set the window size to 400x300 pixels

message_button = tk.Button(root, text="Show Message", command=show_message)
message_button.pack(pady=10)

close_button = tk.Button(root, text="Go Away", command=close_app)
close_button.pack(pady=10)

root.mainloop()