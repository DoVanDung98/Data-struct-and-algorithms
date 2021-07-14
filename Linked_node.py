# Linked list implementation in Python

class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

