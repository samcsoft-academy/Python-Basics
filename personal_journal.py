import os
from datetime import datetime

# Setting up the directory
if not os.path.exists("MyJournal"):
    os.makedirs("MyJournal")

# Create a new journal entry
def create_entry():
    entry_text = input("What's on your mind today? ")
    filename = f"MyJournal/{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(entry_text)
    print(f"Entry saved as {filename}!")

# View all entries
def view_entries():
    entries = os.listdir("MyJournal")
    if entries:
        for entry in entries:
            print(entry)
    else:
        print("No entries found.")

# Read a specific entry
def read_entry(entry_name):
    filepath = f"MyJournal/{entry_name}"
    try:
        with open(filepath, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Entry not found.")

def update_entry(entry_name):
    filepath = f"MyJournal/{entry_name}"
    try:
        with open(filepath, "a") as file:
            new_text = input("What's new on your mind? ")
            file.write("\n" + new_text)
        print(f"Entry {entry_name} updated.")
    except FileNotFoundError:
        print("Entry not found.")

# Sample usage to try out the functions
print("Welcome to your Personal Journal!")
create_entry()
view_entries()
read_entry(input("Which entry would you like to read? "))
update_entry(input("Which entry would you like to edit? "))
