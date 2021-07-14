# Last in first out (LIFO)
'''
    A stack is a linear data structure that follows the principle
    of Last in first out (LIFO).This means the last element inserted
    inside the stack is removed first
'''

# stack implement with python

# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Push item to stack
def push(stack, item):
    stack.append(item)
    print("pushed item: ", item)

# Removing item
def pop(stack):
    if check_empty(stack):
        return 'stack is empty'
    else:
        return stack.pop

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print(stack)
print("popped item: " + stack.pop())
print("stack after popping an element: " + str(stack))

# Stack time complexity
'''
    For the array-based implementation of a stack, the push and pop operations take constant time
    O(1)
'''
