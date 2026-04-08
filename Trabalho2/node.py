class Node: 
    def __init__(self, valor):
        self.value = valor
        self.prio = False
        self.next = None
        

    def __str__(self):
        return str(self.value)
    
    def definePriority(self, priority):
        self.prio = priority