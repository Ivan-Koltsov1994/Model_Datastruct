from scr.stack import Node


class Queue:
    """ Класс для работы со структурой данных Queue"""

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

    def dequeue(self):
        """ Метод удаляет крайний левый элемент данные из Queue """
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return dequeue_element.data

# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')

# print(queue.head.data)
# print(queue.head.next_node.data)
# print(queue.tail.data)
# print(queue.tail.next_node)
# print(queue.tail.next_node.data)


# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
