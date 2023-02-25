import unittest
from scr.datastr import Stack,Node


class TestNode(unittest.TestCase):
    """Тестируем класс Node"""


    def setUp(self) -> None:
        self.node_5 = Node(5)

    def test_node_init(self):
        """Тестируем, что класс инициализируется"""

        assert self.node_5.data == 5
        assert self.node_5.next_node is None

    def test_node_next(self):
        """Тестируем, что есть ссылка на предыдущий  узел"""

        node2 = Node(5, self.node_5)

        assert node2.next_node is self.node_5


