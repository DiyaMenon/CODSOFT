from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(END, f"{task} (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "You must enter a new task to update.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Setting up the main window
root = Tk()
root.title("To-Do List Application")
root.geometry("400x450")
root.config(bg="lightgray")

# Entry widget for entering tasks
task_entry = Entry(root, width=40, borderwidth=2, font=("Arial", 14))
task_entry.pack(pady=10)

# Button to add tasks
add_button = Button(root, text="Add Task", command=add_task,fg="black", font=("Arial", 14))
add_button.pack(pady=5)

# Button to remove tasks
remove_button = Button(root, text="Remove Task", command=remove_task, fg="black", font=("Arial", 14))
remove_button.pack(pady=5)

# Button to mark tasks as completed
complete_button = Button(root, text="Mark as Completed", command=mark_completed, fg="black", font=("Arial", 14))
complete_button.pack(pady=5)

# Button to update tasks
update_button = Button(root, text="Update Task", command=update_task, fg="black", font=("Arial", 14))
update_button.pack(pady=5)

# Listbox to display tasks
listbox = Listbox(root, width=50, height=15, font=("Arial", 12), selectmode=SINGLE)
listbox.pack(pady=10)

root.mainloop()
