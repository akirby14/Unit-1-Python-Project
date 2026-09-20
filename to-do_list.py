def ask_command():
    command = input("Enter a command: ")
    if command == "/help":
        help_command(command)
    

def help_command(command_input):
    print("Available commands:")
    print("/add - Add a new task to the list")
    print("/remove - Remove a task from the list")
    print("/view - View all tasks in the list")
    print("/end program - Exit the program")
    ask_command()
