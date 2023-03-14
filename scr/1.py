class Box:
  def __init__ (self,cat = None):
    self.cat = cat
    self.nextcat = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

ll = LinkedList()
ll.addToEnd({'id': 1})
ll.addToEnd({'id': 2})
ll.addToEnd({'id': 3})
print(ll)