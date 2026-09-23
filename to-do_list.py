def ask_command():
    command = input("Enter a command: ")
    if command == "/help":
        help_command(command)
    elif command == "/add":
            add_command()
    elif command == "/remove":
            remove_command()
    elif command == "/view":
            view_command()
    elif command == "/end program":
            print("Ending program...")
    else:
        print("Invalid command. Please try again.")
        ask_command()

def help_command(command_input):
    print("Available commands:")
    print("/add - Add a new task to the list")
    print("/remove - Remove a task from the list")
    print("/view - View all tasks in the list")
    print("/end program - Exit the program")
    ask_command()

def add_command():
    task = input("Enter the task you want to add: ")
    to_do_list.append(task)
    print(f'Task "{task}" has been added to your To-Do List.')
    ask_command()

def remove_command():
    task = input("Enter the task you want to remove: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print(f'Task "{task}" has been removed from your To-Do List.')
    else:
        print(f'Task "{task}" not found in your To-Do List.')
    ask_command()

def view_command():
    if to_do_list:
        print("Your To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")
    ask_command()

to_do_list = []
print("Welcome to your To-Do List! \nUse the command /help to see the list of available commands.")
ask_command()