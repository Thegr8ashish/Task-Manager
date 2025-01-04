from colorama import Fore, Style

def view_tasks(tasks):
    print(Fore.CYAN + "\n===============================")
    print(Fore.BLUE + "TASK MANAGER")
    print(Fore.CYAN + "===============================")
    if not tasks:
        print("No tasks available.\n")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task.get("completed") else "Pending"
            print(f"{idx}. {task['name']} - {task['description']} | Deadline: {task['deadline']} | Status: {status}")
    print(Style.RESET_ALL)

def add_task(tasks):
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    tasks.append({"name": name, "description": description, "deadline": deadline, "completed": False})
    print("Task added successfully.")

def edit_task(tasks):
    try:
        view_tasks(tasks)
        task_idx = int(input("Enter the task number you want to edit: ")) - 1
        if 0 <= task_idx < len(tasks):
            name = input("Enter new task name: ")
            description = input("Enter new task description: ")
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks[task_idx].update({"name": name, "description": description, "deadline": deadline})
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def delete_task(tasks):
    try:
        choice = input("Do you want to delete a single task or multiple? (single/multiple): ").lower()
        if choice == "multiple":
            task_numbers = input("Enter task numbers to delete (comma separated): ")
            task_numbers = [int(num.strip()) - 1 for num in task_numbers.split(",")]
            tasks_to_delete = [task for idx, task in enumerate(tasks) if idx in task_numbers]
            for task in tasks_to_delete:
                tasks.remove(task)
            print("Tasks deleted successfully.")
        elif choice == "single":
            task_number = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks.pop(task_number)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def mark_completed(tasks):
    try:
        choice = input("Do you want to mark a single task or multiple as completed? (single/multiple): ").lower()
        if choice == "multiple":
            task_numbers = input("Enter task numbers to mark as completed (comma separated): ")
            task_numbers = [int(num.strip()) - 1 for num in task_numbers.split(",")]
            for task in tasks:
                if task in [tasks[idx] for idx in task_numbers]:
                    task['completed'] = True
            print("Tasks marked as completed.")
        elif choice == "single":
            task_number = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]['completed'] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
