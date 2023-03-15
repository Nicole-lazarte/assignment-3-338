import sys

# Define a stack class using linked list implementation
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

# Define a function that evaluates an S-expression and returns its result
def evaluate(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
            elif token == '*':
                stack.push(op1 * op2)
            elif token == '/':
                stack.push(op1 / op2)
        elif token == '(':
            pass
        elif token == ')':
            pass
        else:
            raise ValueError("Invalid token: " + token)
    if stack.is_empty():
        raise ValueError("Empty expression")
    result = stack.pop()
    if not stack.is_empty():
        raise ValueError("Incomplete expression")
    return result

# Get the expression from the command line argument
expression = sys.argv[1]

# Evaluate the expression and print the result
result = evaluate(expression)
print(result)
