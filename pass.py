import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Generates a random password based on the user-defined length."""
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6.")
            return

        
        characters = string.ascii_letters + string.digits + string.punctuation
        
     
        password = ''.join(random.choice(characters) for _ in range(length))
        
        
        pass_entry.delete(0, tk.END)
        pass_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    """Copies the generated password to the clipboard."""
    window.clipboard_clear()
    window.clipboard_append(pass_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")


window = tk.Tk()
window.title("Simple Password Generator")
window.geometry("360x250")
window.config(padx=20, pady=20)


length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, pady=10, sticky="w")

length_entry = tk.Entry(window, width=10)
length_entry.grid(row=0, column=1, pady=10, sticky="w")
length_entry.insert(0, "12") 


generate_btn = tk.Button(window, text="Generate Password", command=generate_password)
generate_btn.grid(row=1, column=0, columnspan=2, pady=10)


pass_entry = tk.Entry(window, width=30, font=("Arial", 12))
pass_entry.grid(row=2, column=0, columnspan=2, pady=10)


copy_btn = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.grid(row=3, column=0, columnspan=2, pady=10)


window.mainloop()