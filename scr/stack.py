class Node:
    """ Создаем и инициализируем узел данных """

    def __init__(self, data, next_node=None):
        self.data = data  # тут данные
        self.next_node = next_node  # тут ссылка на следующий


class Stack:
    """ Класс для работы с типом данных Stack """
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Метод добавляет данные в СТЭК """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """ Метод удаляет данные из СТЭКа """
        if self.top is None:
            raise Exception("СТЭК пустой")
        remove = self.top
        self.top = self.top.next_node
        return remove

# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# data = stack.pop()

# теперь последний элемента содержит данные data1
# print(stack.top.data)
