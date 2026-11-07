import unittest

from todo.search import search_by_priority
from todo.task import Task


class TestSearchPriority(unittest.TestCase):
    def test_search_by_priority(self):
        items = [Task("a", 1), Task("b", 2), Task("c", 2)]
        result = search_by_priority(items, 2)
        self.assertEqual([t.title for t in result], ["b", "c"])
