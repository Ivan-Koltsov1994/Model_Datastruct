from inspect import stack


class Node:

    def __init__(self,data, next_node =None):
        self.data = data # атрибут для хранения данных
        self.next_node = next_node # атрибут для хранения ссылки на следующий узел

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Метод добавляет данные в СТЭК """
        current_top = stack.top
        stack.top = Node(data)
        stack.top.next_node = current_top


#n1 = Node(5, None)
#n2 = Node('a', n1)
#print(n1.data)
#print(n2.data)
#print(n1)
#print(n2.next_node)

#stack = Stack()
#stack.push('data1')
#stack.push('data2')
#stack.push('data3')
#print(stack.top)
#print(stack.top.next_node.data)
#print(stack.top.next_node.next_node.data)
#print(stack.top.next_node.next_node.next_node)
#print(stack.top.next_node.next_node.next_node.data)
