from todo_list import ToDoList


def test_add_task(tmp_path):
    todo = ToDoList(tmp_path / "test_tasks.json")
    todo.add_task("Homework")

    assert "Homework" in todo.tasks


def test_remove_task(tmp_path):
    todo = ToDoList(tmp_path / "test_tasks.json")
    todo.add_task("Homework")
    todo.remove_task("Homework")

    assert "Homework" not in todo.tasks


def test_empty_list(tmp_path):
    todo = ToDoList(tmp_path / "test_tasks.json")

    assert todo.tasks == []


def test_saved_tasks_load(tmp_path):
    filename = tmp_path / "test_tasks.json"

    todo = ToDoList(filename)
    todo.add_task("Study calculus")

    new_todo = ToDoList(filename)

    assert "Study calculus" in new_todo.tasks