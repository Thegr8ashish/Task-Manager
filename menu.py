import sys
from task_manager import view_tasks, add_task, edit_task, delete_task, mark_completed
from file_handler import save_tasks
from colorama import Fore, Style

def menu(tasks):
    while True:
        # Task Manager title with color
        print(Fore.CYAN + "===============================")
        print(Fore.BLUE + "TASK MANAGER")
        print(Fore.CYAN + "===============================")
        
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                edit_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                mark_completed(tasks)
            elif choice == 6:
                save_tasks(tasks)  # Save tasks before exiting
                print("Exiting...")
                os.exit(0)
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a valid number.")
