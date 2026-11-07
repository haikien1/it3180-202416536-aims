import unittest

from todo.task import Task
from todo.todolist import TodoList


class TestFilter(unittest.TestCase):
    def test_filter_by_min_priority(self):
        todo = TodoList()
        todo.add(Task("low", 1))
        todo.add(Task("high", 3))
        result = todo.filter_by_min_priority(2)
        self.assertEqual([t.title for t in result], ["high"])
