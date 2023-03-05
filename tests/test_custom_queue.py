import unittest
from scr.custom_queue import Queue


class TestQueue(unittest.TestCase):
    """Тестируем класс Queue"""

    def setUp(self) -> None:
        self.queue = Queue()

    def test_queue_init(self):
        """Тестируем, что класс инициализируется"""
        self.queue.enqueue(5)
        assert self.queue.head.data == 5

    def test_node_next(self):
        """Тестируем, что есть ссылка на следующий элемент"""
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        assert self.queue.head.data == 5
        assert self.queue.tail.data == 6