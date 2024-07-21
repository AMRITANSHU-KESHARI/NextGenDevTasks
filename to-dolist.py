import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{idx + 1}. {task['task']} - {status}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
        else:
            print("Invalid task number.")

    def menu(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add task")
            print("2. View tasks")
            print("3. Complete task")
            print("4. Delete task")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                task = input("Enter task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_number = int(input("Enter task number to mark as completed: "))
                self.complete_task(task_number)
            elif choice == '4':
                task_number = int(input("Enter task number to delete: "))
                self.delete_task(task_number)
            elif choice == '5':
                print("Exiting the application.")
                sys.exit()
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()

