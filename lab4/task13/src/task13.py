class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.first = None  

    def isEmpty(self):
        return self.first is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.first
        self.first = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped_data = self.first.data
        self.first = self.first.next
        return popped_data

    def __repr__(self):
        elements = []
        current = self.first
        while current:
            elements.append(current.data)
            current = current.next
        return " ".join(map(str, elements))


class Queue:
    def __init__(self, max_size = None):
        self.front = None  
        self.back = None
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        if self.max_size == None:
            return False
        return self.size >= self.max_size

    def enqueue(self, value):
        if self.isFull():
            return
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = self.back.next
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        self.front = self.front.next
        if self.front is None:
            self.back = None
        self.size -= 1

    def __repr__(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return " ".join(map(str, elements))