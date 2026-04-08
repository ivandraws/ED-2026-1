from node import Node

class Fila:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def dequeue(self):
        aux = self.head
        if not self.isEmpty():
            if aux.next == None:
                value = aux.value
                return value
            while True:
                if aux.next.next !=  None:
                    aux = aux.next
                else:
                    value = aux.next.value
                    aux.next = None
                    return value
        else: 
            return None

    def show(self):
        print("final <- ", end='')
        aux = self.head
        while True:
            print(f"{aux} <- ", end='' )
            if aux.next == None:
                break
            else: 
                aux = aux.next
        
        print("HEAD")

    def firstQueue(self):
        return self.head.value

    def len(self):
        size = 0
        aux = self.head 
        while aux.next != None: 
            size += 1
            aux = aux.next
    

    def isEmpty(self):
        return self.head is None