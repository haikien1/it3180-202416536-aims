import unittest

from todo.task import Task
from todo.todolist import MAX_TASKS, TodoList


class TestTodoList(unittest.TestCase):
    def test_add_until_full(self):
        todo = TodoList()
        for i in range(MAX_TASKS):
            self.assertTrue(todo.add(Task(f"task {i}")))
        self.assertFalse(todo.add(Task("one too many")))

    def test_pending_count(self):
        todo = TodoList()
        todo.add(Task("a"))
        todo.add(Task("b"))
        todo.complete("a")
        self.assertEqual(todo.pending_count(), 1)
