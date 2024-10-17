# Task Manager CLI Application

The *Task Manager CLI* is a simple command-line interface (CLI) application written in Python. It allows users to efficiently manage tasks by adding, viewing, marking them as complete, deleting, and saving/loading tasks from a JSON file for persistent storage.

## Features

- *Add a Task*: Create a new task by providing a title.
- *View Tasks*: View the list of all tasks with their completion status (completed or not).
- *Delete a Task*: Remove a task from the list by its ID.
- *Mark Task as Complete*: Mark a task as completed by its ID.
- *Save and Load Tasks*: Save tasks to a JSON file (tasks.json) and load them automatically when the program starts.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository or download the project files:

    bash
    git clone <repository-url>
    

    (Or download the zip file and extract it.)

2. Navigate to the project directory:

    bash
    cd task_manager
    

### Running the Application

To run the Task Manager CLI application, use the following command in your terminal:

bash
python task_manager.py


## Usage Instructions

Once the program starts, you will see a menu with the following options:
### Menu Options:

1. *Add Task* - Allows you to add a new task to the list.
2. *View Tasks* - Displays the current list of tasks.
3. *Delete Task* - Deletes a task from the list by its index.
4. *Mark Task as Complete* - Marks a specific task as complete.
5. *Save & Exit* - Saves the task list and exits the program.
6. *Exit without Saving* - Exits the program without saving changes.

### Menu Options:

1. *Add Task*:  
   Select option 1 and enter the title of the task you want to add.

2. *View Tasks*:  
   Select option 2 to view the list of tasks. Completed tasks are marked with a "✓", and incomplete tasks with a "✗".

3. *Delete Task*:  
   Select option 3 and enter the ID of the task you wish to delete.

4. *Mark Task as Complete*:  
   Select option 4 and enter the ID of the task you want to mark as completed.

5. *Save & Exit*:  
   Select option 5 to save the current task list to tasks.json and exit the program.

6. *Exit without Saving*:  
   Select option 6 to exit the program without saving any changes.

# Project Structure

The project structure looks like this:

task_manager/

├── task_manager.py # Main Python script with CLI functionality 

├── tasks.json # JSON file for saving tasks (auto-generated) 

└── README.md # Project documentation

# Example Usage

## Task Manager CLI

1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save & Exit
6. Exit without Saving

### Choose an option: 1  
Enter task title: Complete Python Assignment  
Task added successfully!

### Choose an option: 2  
1. Complete Python Assignment [✗]

## Saving Tasks

The tasks are saved in a tasks.json file in the same directory. Each task has the following structure:

json
[
    {
        "id": 1,
        "title": "Complete Python Assignment",
        "completed": false
    }
]



## Technologies Used

- *Python*: The core language used to build this CLI application.
- *JSON*: Used for saving and loading tasks to and from a file.

## License
 This project is open-source and available under the MIT License.
