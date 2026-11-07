from task import Task
from todolist import TodoList


def main():
    todo = TodoList()
    todo.add(Task("Learn Git", 1))
    todo.add(Task("Write report", 2))
    todo.add(Task("Submit lab", 3))
    todo.complete("Learn Git")
    print("Pending tasks:", todo.pending_count())


if __name__ == "__main__":
    main()
