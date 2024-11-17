import tkinter as tk
import random

def show_dialog():
    for _ in range(20):
        dialog = tk.Toplevel(root)
        dialog.geometry(f"200x100+{random.randint(0, root.winfo_screenwidth()-200)}+{random.randint(0, root.winfo_screenheight()-100)}")
        tk.Label(dialog, text="This is a dialog box").pack()
        #dialog.after(2000, dialog.destroy)  # Close the dialog after 2 seconds

root = tk.Tk()
# Add a button to the middle of the dialog
button = tk.Button(root, text="Check for Virus", command=show_dialog)
button.pack(expand=True)
root.title("Main Window")

root.geometry("600x600")
#root.withdraw()  # Hide the root window
#show_dialog()
root.mainloop()
