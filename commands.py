def help_command():
    print("Available commands:")
    print("/add - Add a new task to the list")
    print("/remove - Remove a task from the list")
    print("/view - View all tasks in the list")
    print("/end program - Exit the program")


def add_command(todo_list):
    task = input("Enter the task you want to add: ")
    todo_list.add_task(task)


def remove_command(todo_list):
    task = input("Enter the task you want to remove: ")
    todo_list.remove_task(task)


def view_command(todo_list):
    todo_list.view_tasks()
