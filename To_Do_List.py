def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks in your list.")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    show_tasks(tasks)

    try:
        task_num = int(input("Enter the task number to remove: "))
        if task_num >= 1 and task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

main()