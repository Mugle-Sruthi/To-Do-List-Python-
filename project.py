import datetime
import time


tasks = []


def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"title": title, "description": description, "due_date": due_date, "completed": False})
    print("Task added successfully!")


def display_tasks():
    print("\nTask List:")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. Title: {task['title']}\tDue Date: {task['due_date']}\tStatus: {status}")


def mark_completed():
    display_tasks()
    choice = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid choice.")


def set_reminders():
    while True:
        current_time = datetime.datetime.now()
        for task in tasks:
            due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d")
            if not task["completed"] and current_time.date() == due_date.date():
                print(f"Reminder: Task '{task['title']}' is due today!")
        
        time.sleep(60) 


def main():
    print("Task Manager and Reminder")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Set Reminders")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            set_reminders()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()