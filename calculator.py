import tkinter as tk
from tkinter import messagebox

# Initialize the task list
tasks = []

def add_task():
    """Add a new task to the list."""
    task = task_entry.get()
    if task.strip():
        tasks.append({"task": task, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def delete_task():
    """Delete the selected task."""
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed():
    """Mark the selected task as completed."""
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def update_task_list():
    """Update the task list display."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Input for adding tasks
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12), bg="lightgreen")
add_button.pack(pady=5)

# Task list display
task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)

# Action buttons
mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, font=("Arial", 12), bg="lightblue")
mark_completed_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 12), bg="lightcoral")
delete_button.pack(pady=5)

# Run the application
root.mainloop()