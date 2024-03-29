from scr.stack import Node


class LinkedList:
    """ Класс для работы со структурой данных LinkedList(односвязный список)"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные и добавляет узел с этими данными в начало односвязного списка"""
        check_data = self.check_data(data)
        if check_data is not None:
            new_node = Node(check_data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next_node = self.head
                self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные и добавляет узел с этими данными в конец односвязного списка"""
        check_data = self.check_data(data)
        if check_data is not None:
            new_node = Node(check_data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node

    @staticmethod
    def check_data(data):
        """Проверяет, что данные это словарь, который содержит ключ ['id]"""
        try:
            if not isinstance(data, dict):
                raise TypeError
            else:
                if 'id' not in list(data.keys()):
                    raise TypeError
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')
        else:
            return data

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

    def to_list(self):
        """ Метод ввозвращает список с данными, содержащимися в односвязном списке  """
        ll_list = []
        node = self.head
        if node is None:
            return None
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, value):
        """Возвращает первый найденный в LinkedList словарь с ключом id,
        значение которого равно переданному в метод значению"""
        try:
            ll_list = self.to_list()
            for item in ll_list:
                if item['id'] == value:
                    return item
            raise ValueError
        except ValueError:
            return None


#ll = LinkedList()

#ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
#ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
#ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
#ll.insert_beginning({'id': 0, 'username': 'serebro'})

# метод to_list()
#lst = ll.to_list()
#for item in lst: print(item)


# get_data_by_id()
#user_data = ll.get_data_by_id(3)
#print(user_data)


# работа блока try/except
#ll = LinkedList()
#ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
#ll.insert_at_end('idusername')
#ll.insert_at_end([1, 2, 3])
#ll.insert_at_end({'id': 2, 'username': 'mosh_s'})


#user_data = ll.get_data_by_id(2)
#print(user_data)
