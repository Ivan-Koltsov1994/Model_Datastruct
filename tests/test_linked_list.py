from scr.linked_list import LinkedList
import unittest


class TestLinked(unittest.TestCase):
    """Тестируем класс LinkedList"""

    def test_linked_insert_beginning(self):
        """Тестируем, что данные ложатся в LinkedList"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        assert ll.head is not None
        self.assertEqual(ll.tail.next_node, None)

    def test_linked_insert_at_end_none(self):
        """Тестируем, что данные ложатся в LinkedList при пустой структуре данных"""
        ll = LinkedList()
        ll.insert_at_end({'id': 1})
        assert ll.head is not None

    def test_linked_get_data_by_id(self):
        """Тестируем получение первого найденного словаря по переданному значению"""

        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        self.assertEqual(ll.get_data_by_id(3), {'id': 3})
        self.assertEqual(ll.get_data_by_id(4), None)

    def test_check_linked_list(self):
        """Тестируем правильность хранения ссылок"""

        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.head.next_node.next_node.data, {'id': 2})
        self.assertEqual(ll.head.next_node.next_node.next_node.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)

    def test_linked_insert_incorrect_element(self):
        """Ожидается обработка исключения TypeError при добавлении некорректного элемента"""
        ll = LinkedList()
        result = 'Данные не являются словарем или в словаре нет id.'
        self.assertEqual(ll.insert_beginning([1, 2, 3]), print(result))
        self.assertEqual(ll.insert_at_end({'one': 1}), print(result))