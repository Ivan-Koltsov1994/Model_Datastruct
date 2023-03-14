from scr.stack import Node


class LinkedList:
    """ Класс для работы со структурой данных LinkedList(односвязный список)"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        """ Метод принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка """
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        """ Метод принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка """
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next_node:
            itr = itr.next_node
        itr.next_node = Node(data, None)

    def print_ll(self):
        """ Метод выводящий в консоль данные из односвязанного списка """
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
