import tkinter as tk
from tkinter import messagebox
import os

# File where slam book entries will be stored
DATA_FILE = "slam_book.txt"

# Function to save entry
def save_entry():
    name = name_entry.get().strip()
    nickname = nickname_entry.get().strip()
    hobby = hobby_entry.get().strip()
    memory = memory_text.get("1.0", tk.END).strip()

    # Input validation
    if not name or not nickname or not hobby or not memory:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    try:
        with open(DATA_FILE, "a", encoding="utf-8") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Nickname: {nickname}\n")
            file.write(f"Hobby: {hobby}\n")
            file.write(f"Memory: {memory}\n")
            file.write("-" * 40 + "\n")
        messagebox.showinfo("Success", "Entry saved successfully!")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Could not save entry: {e}")

# Function to clear fields
def clear_fields():
    name_entry.delete(0, tk.END)
    nickname_entry.delete(0, tk.END)
    hobby_entry.delete(0, tk.END)
    memory_text.delete("1.0", tk.END)

# Function to view all entries
def view_entries():
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("Info", "No entries found yet.")
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            content = file.read()
        # Show entries in a new window
        view_window = tk.Toplevel(root)
        view_window.title("Slam Book Entries")
        text_area = tk.Text(view_window, wrap=tk.WORD, width=60, height=20)
        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)
        text_area.pack(padx=10, pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not read entries: {e}")

# Main window
root = tk.Tk()
root.title("Slam Book")
root.geometry("400x500")

# Labels and fields
tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=2)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)

tk.Label(root, text="Nickname:").pack(anchor="w", padx=10, pady=2)
nickname_entry = tk.Entry(root, width=40)
nickname_entry.pack(padx=10)

tk.Label(root, text="email:").pack(anchor="w", padx=10, pady=2)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=10)

tk.Label(root, text="Memory:").pack(anchor="w", padx=10, pady=2)
memory_text = tk.Text(root, width=40, height=5)
memory_text.pack(padx=10)

# Buttons
tk.Button(root, text="Save Entry", command=save_entry, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields, bg="lightyellow").pack(pady=5)
tk.Button(root, text="View Entries", command=view_entries, bg="lightblue").pack(pady=5)

root.mainloop()
