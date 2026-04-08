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
                aux = aux.next
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
        aux = self.head 
        while True:
            if self.isEmpty():
                return None
            elif aux.next == None:
                return aux.value
            else:
                aux = aux.next

    def len(self):
        size = 0
        aux = self.head 
        while aux != None: 
            size += 1
            aux = aux.next
        return size
    

    def isEmpty(self):
        return self.head is None