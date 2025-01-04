# Task Manager 📋
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![IDE](https://img.shields.io/badge/VSCode-1.84+-blue.svg)](https://code.visualstudio.com/)

> A user-friendly desktop application that helps you manage and organize your daily tasks. Created as a Python Programming project at IIT MANDI, Masai School.

## 📁 Table of Contents
- [Features](#-features)
- [Simple Installation Guide](#-simple-installation-guide)
- [How to Use](#-how-to-use)
- [Project Details](#-project-details)
- [Demo Video](#-demo-video)
- [Contact](#-contact)

## ✨ Features
- See all your tasks in one place
- Add new tasks easily
- Edit task details
- Delete one or many tasks at once
- Mark single or multiple tasks as completed
- Tasks are saved when exiting properly (using option 6)
- **Run the program with one click** using the `.bat` file (requires Python and Colorama installed)
- Colorful and easy-to-read display
- Error handling for:
  - Invalid menu selections
  - Non-existent task numbers
  - Invalid input types
  - Batch operations (multiple task deletion/completion)

## 🚀 Simple Installation Guide

### Step 1: Install Python
1. Go to [Python's website](https://www.python.org/downloads/)
2. Click the big "Download Python" button
3. Run the downloaded file
4. **Important**: Check "Add Python to PATH" during installation
5. Click Install

### Step 2: Get the Task Manager
1. Click the green "Code" button on [this page](https://github.com/Thegr8ashish/Task-Manager)
2. Click "Download ZIP"
3. Unzip the file to your desired location

### Step 3: Install Required Package
1. Open Command Prompt (Windows) or Terminal (Mac)
2. Copy and paste this command:
```bash
pip install colorama
```

### Step 4: Run the Program

#### Option 1: Using the `.bat` file
- Navigate to the unzipped folder
- Double-click the `run_task_manager.bat` file
- **Note**: You may see a Windows Defender SmartScreen warning saying "Windows protected your PC" because the .bat file is from an unknown publisher. This is normal for custom scripts. You have two options:
  1. Click "More info" and then "Run anyway" if you trust the source
  2. Alternatively, you can run the program using Option 2 below to avoid the warning

#### Option 2: Using Python Manually
- Open Command Prompt/Terminal in the folder
- Run the program with:
```bash
python main.py
```

## 💻 How to Use
When you start the program, you'll see this menu:
```
===============================
       TASK MANAGER
===============================
1. View Tasks
2. Add Task
3. Edit Task
4. Delete Task
5. Mark Task Completed
6. Exit
```

### Important Note:
- Tasks are saved when you exit the program using option 6

### Basic Operations:
1. Press 1 to see your tasks
2. Press 2 to add a new task
3. Press 3 to change a task
4. Press 4 to remove tasks
   - Choose single or multiple task deletion
   - For multiple tasks, enter numbers separated by commas
5. Press 5 to mark tasks as done
   - Choose single or multiple task completion
   - For multiple tasks, enter numbers separated by commas
6. Press 6 to save and exit

## 📁 Project Details
Files included:
- `main.py` - Starts the program
- `menu.py` - Shows the menu
- `task_manager.py` - Handles tasks
- `file_handler.py` - Saves your tasks
- `tasks.json` - Where your tasks are stored
- `run_task_manager.bat` - One-click script to run the program

## 🎥 Demo Video
[Watch how it works](https://youtu.be/fBnugI9nbF8)

The video shows:
1. How to install and start 
2. All features in action 

## 📧 Contact
Created by Ashish Kumar 
- GitHub: [@Thegr8ashish](https://github.com/Thegr8ashish)
- Project Link: [Task Manager](https://github.com/Thegr8ashish/Task-Manager)

## 🎓 Academic Project
This Task Manager was created as a project for the Python Programming course at IIT MANDI, Masai School.
