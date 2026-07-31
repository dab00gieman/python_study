# TO-DO LIST MANAGER
# Built this to practice lists, dictionaries, and file handling
# Still figuring out how to make it look pretty lol

# I'll store tasks as a list of dictionaries
# Each task: {"task": "something", "done": False}
todo_list = []

# Load saved tasks if file exists - I learned this from a YouTube video
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                # Strip newline and split by '|' 
                # I used '|' because commas might be in the task name
                parts = line.strip().split("|")
                if len(parts) == 2:
                    task_name = parts[0]
                    done_status = parts[1] == "True"
                    todo_list.append({"task": task_name, "done": done_status})
        print("📂 Loaded your saved tasks!\n")
    except FileNotFoundError:
        # First time running - no file yet
        print("📝 No saved tasks found. Starting fresh!\n")

# Save tasks to file - I call this after every change so I don't lose anything
def save_tasks():
    with open("tasks.txt", "w") as file:
        for item in todo_list:
            file.write(f"{item['task']}|{item['done']}\n")
    print("💾 Tasks saved!")

# Show all tasks with nice formatting
def show_tasks():
    if not todo_list:
        print("📭 Your to-do list is empty! Add something.")
        return
    
    print("\n" + "=" * 45)
    print("  YOUR TO-DO LIST")
    print("=" * 45)
    
    for index, item in enumerate(todo_list, start=1):
        # I used emojis to make it more fun
        status = "✅" if item["done"] else "⬜"
        print(f"{index}. {status} {item['task']}")
    
    print("=" * 45 + "\n")

# Add a new task
def add_task():
    task_name = input("📝 Enter task description: ")
    if task_name.strip() == "":
        print("❌ Task can't be empty!\n")
        return
    
    todo_list.append({"task": task_name, "done": False})
    print(f"✅ Added: '{task_name}'")
    save_tasks()

# Mark a task as done
def complete_task():
    show_tasks()
    if not todo_list:
        return
    
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(todo_list):
            todo_list[choice - 1]["done"] = True
            print(f"🎉 Marked as done: '{todo_list[choice - 1]['task']}'")
            save_tasks()
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a number!")

# Delete a task - I was scared to add this at first lol
def delete_task():
    show_tasks()
    if not todo_list:
        return
    
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(todo_list):
            removed = todo_list.pop(choice - 1)
            print(f"🗑️ Deleted: '{removed['task']}'")
            save_tasks()
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a number!")

# THE MAIN MENU - this is where everything runs
def main():
    load_tasks()
    
    while True:
        print("\n" + "-" * 30)
        print("  📋 TO-DO LIST MENU")
        print("-" * 30)
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Exit")
        print("-" * 30)
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\n👋 Goodbye! Your tasks are saved.")
            save_tasks()
            break  # This exits the loop - took me a while to figure out
        else:
            print("❌ Invalid choice! Pick 1-5.")

# This runs the program - my teacher said always include this
if __name__ == "__main__":
    main()