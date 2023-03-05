from scr.stack import Node


class Queue:
    """ Класс для работы с структурой данных Queue"""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """ Метод добавляет данные в Queue """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')

# print(queue.head.data)
# print(queue.head.next_node.data)
# print(queue.tail.data)
# print(queue.tail.next_node)
# print(queue.tail.next_node.data)
