from scr.linked_list import LinkedList
import unittest


class TestLinked(unittest.TestCase):
    """Тестируем класс LinkedList"""

    def test_linked_insert_beginning(self):
        """Тестируем, что данные ложатся в LinkedList"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 2})
        assert ll.head is not None

    def test_linked_insert_at_end_none(self):
        """Тестируем, что данные ложатся в LinkedList при пустой структуре данных"""
        ll = LinkedList()
        ll.insert_at_end({'id': 1})
        assert ll.head is not None
