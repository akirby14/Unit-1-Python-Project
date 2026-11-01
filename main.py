from todo_list import ToDoList

from commands import (
    help_command,
    add_command,
    remove_command,
    view_command
)


def ask_command(todo_list):
    while True:
        command = input("\nEnter a command: ")

        if command == "/help":
            help_command()

        elif command == "/add":
            add_command(todo_list)

        elif command == "/remove":
            remove_command(todo_list)

        elif command == "/view":
            view_command(todo_list)

        elif command == "/end program":
            print("Ending program...")
            break

        else:
            print("Invalid command. Please try again.")


my_list = ToDoList()

print("Welcome to your To-Do List!")
print("Use the command /help to see the list of available commands.")

ask_command(my_list)