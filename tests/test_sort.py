import unittest

from todo.task import Task
from todo.todolist import TodoList


class TestSort(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()
        for title, p in [("b task", 1), ("A task", 3), ("c task", 2)]:
            self.todo.add(Task(title, p))

    def test_sort_by_title(self):
        self.todo.sort_by_title()
        self.assertEqual([t.title for t in self.todo.items],
                         ["A task", "b task", "c task"])

    def test_sort_by_priority(self):
        self.todo.sort_by_priority()
        self.assertEqual([t.priority for t in self.todo.items], [3, 2, 1])
