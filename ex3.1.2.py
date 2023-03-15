class Stack:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None
    
    def push(self, data):
        self.head = self.Node(data, self.head)
    
    def pop(self):
        if self.head is None:
            raise ValueError("Stack is empty")
        data = self.head.data
        self.head = self.head.next
        return data
    
    def peek(self):
        if self.head is None:
            raise ValueError("Stack is empty")
        return self.head.data
    
    def is_empty(self):
        return self.head is None
