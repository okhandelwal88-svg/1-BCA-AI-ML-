import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

def add_task():
    task = task_entry.get()
    if task :
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index] = tasks[selected_index] + " ✔"
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark done!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark Done", command=mark_done)
done_button.pack(pady=5)


task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)


root.mainloop()