# Queue data structure
'''
    A queue is a useful data structue in programming.It is similar to the ticket queue outside
    a cinemal hall.
    Queue follows the Fist in Fist out (FIFO) rule - the item that goes in first is the item
    that comes out first
'''

# Implement Queue
class Queue:
    def __init__(self):
        self.queue = []
    
    # add an element
    def enqueue(self, item):
        self.queue.append(item)
    
    # remove an elemnt
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    
    # display the queue
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()


# Complexity Analysis
'''
    The complexity of enque and dequeue operation in a queue using a array is 0(1)
    If use pop(N) in python code, then complexity might be O(n) depending on the 
    position of the item poped
'''