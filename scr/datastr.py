
class Node:
    """ Создаем и инициализируем узел данных """
    def __init__(self, data, next_node = None):
        self.data = data  # тут данные
        self.next_node = next_node # тут ссылка на следующий

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Метод добавляет данные в СТЭК """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

