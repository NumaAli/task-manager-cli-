# task_manager.py
tasks = []  # Ye list me saare tasks store honge

def add_task(task):
    """Add a new task"""
    if task.strip() == "":
        print("Task cannot be empty!")
        return
    tasks.append(task)
    print(f"Task added: {task}")

# CLI interface for add-task only
def main():
    while True:
        print("\nOptions: add / exit")
        choice = input("Enter option: ").strip().lower()

        if choice == "add":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Use 'add' or 'exit'.")

# Gracefully handle Ctrl + C
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
