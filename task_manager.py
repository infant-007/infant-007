import json

class Task:
    def _init_(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['title'], data['completed'])


tasks = []

def add_task(title):
    task_id = len(tasks) + 1
    task = Task(task_id, title)
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "✓" if task.completed else "✗"
            print(f"{task.id}. {task.title} [{status}]")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]

def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            break

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks_data = json.load(f)
            tasks = [Task.from_dict(task) for task in tasks_data]
    except FileNotFoundError:
        tasks = []

def display_menu():
    print("\nTask Manager CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Save & Exit")
    print("6. Exit without Saving")

def main():
    load_tasks()
    while True:
        display_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_id)
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Exiting...")
            break
        elif choice == "6":
            print("Exiting without saving...")
            break
        else:
            print("Invalid option. Please choose a valid one.")

if _name_ == "_main_":
    main()
