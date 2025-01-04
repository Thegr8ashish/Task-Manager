from file_handler import load_tasks, save_tasks
from menu import menu

def main():
    tasks = load_tasks()  # Load tasks from the file

    # Main menu loop
    menu(tasks)

    # Save tasks back to the file when the program ends
    save_tasks(tasks)

if __name__ == "__main__":
    main()
