import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and phone are required.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    search_term = search_entry.get()
    if search_term:
        results = []
        for name, details in contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                results.append(f"{name} - {details['phone']}")
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No contacts found.")
    else:
        messagebox.showwarning("Warning", "Enter a name or phone number to search.")

def select_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index).split(" - ")[0]
        details = contacts[selected_contact]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected_contact)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, details['phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, details['email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, details['address'])
    except IndexError:
        pass

def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name] = {
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

# Load contacts from file
contacts = load_contacts()

# Setting up the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")
root.config(bg="lightblue")

# Frames for organization
top_frame = tk.Frame(root, bg="lightblue")
top_frame.pack(pady=10)

middle_frame = tk.Frame(root, bg="lightblue")
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(root, bg="lightblue")
bottom_frame.pack(pady=10)

# Contact form
name_label = tk.Label(top_frame, text="Name:", font=("Arial", 14), bg="lightblue")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(top_frame, width=30, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(top_frame, text="Phone:", font=("Arial", 14), bg="lightblue")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(top_frame, width=30, font=("Arial", 14))
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(top_frame, text="Email:", font=("Arial", 14), bg="lightblue")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(top_frame, width=30, font=("Arial", 14))
email_entry.grid(row=2, column=1, padx=5, pady=5)

address_label = tk.Label(top_frame, text="Address:", font=("Arial", 14), bg="lightblue")
address_label.grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(top_frame, width=30, font=("Arial", 14))
address_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(top_frame, text="Add Contact", command=add_contact, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 14))
add_button.grid(row=4, column=0, padx=5, pady=10, columnspan=2)

update_button = tk.Button(top_frame, text="Update Contact", command=update_contact, bg="#FFC107", fg="#FFFFFF", font=("Arial", 14))
update_button.grid(row=5, column=0, padx=5, pady=10, columnspan=2)

delete_button = tk.Button(top_frame, text="Delete Contact", command=delete_contact, bg="#f44336", fg="#FFFFFF", font=("Arial", 14))
delete_button.grid(row=6, column=0, padx=5, pady=10, columnspan=2)

# Contact list
contact_list = tk.Listbox(middle_frame, width=50, height=10, font=("Arial", 12))
contact_list.pack(side=tk.LEFT, fill=tk.BOTH, padx=(10, 0))
contact_list.bind("<<ListboxSelect>>", select_contact)

scrollbar = tk.Scrollbar(middle_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
contact_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_list.yview)

# Search bar
search_label = tk.Label(bottom_frame, text="Search:", font=("Arial", 14), bg="lightblue")
search_label.grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(bottom_frame, width=30, font=("Arial", 14))
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(bottom_frame, text="Search", command=search_contact, bg="#2196F3", fg="#FFFFFF", font=("Arial", 14))
search_button.grid(row=0, column=2, padx=5, pady=5)

# Initialize the contact list
update_contact_list()

root.mainloop()
