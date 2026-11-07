import unittest

from todo.search import search_by_title
from todo.task import Task


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.items = [Task("Learn Git"), Task("Write report")]

    def test_search_exact_case(self):
        result = search_by_title(self.items, "Git")
        self.assertEqual([t.title for t in result], ["Learn Git"])

    def test_search_no_match(self):
        self.assertEqual(search_by_title(self.items, "xyz"), [])
