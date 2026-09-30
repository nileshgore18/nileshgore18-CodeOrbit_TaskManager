# CodeOrbit Tech - Task 2
# Simple CLI-Based Task Manager
# Language: Python

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "completed": False})
    print("Task added successfully.")

def complete_task():
    show_tasks()
    if not tasks:
        return
    try:
        number = int(input("Enter task number to complete: "))
        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return
        tasks[number - 1]["completed"] = True
        print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        number = int(input("Enter task number to delete: "))
        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return
        removed = tasks.pop(number - 1)
        print(f"Deleted: {removed['title']}")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using Task Manager!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
