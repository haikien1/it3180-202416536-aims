from todo import __version__
from todo.task import Task
from todo.todolist import TodoList


def main():
    print(f"TODO-mini v{__version__}")
    todo = TodoList()
    todo.add(Task("Learn Git", 1))
    todo.add(Task("Write report", 2))
    todo.add(Task("Submit lab", 3))
    todo.complete("Learn Git")
    todo.print_list()
    print("Pending tasks:", todo.pending_count())


if __name__ == "__main__":
    main()
