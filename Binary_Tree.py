# Binary Tree in Python

'''
    define postorder, preorder, inorder:
        Preorder : traverse finish left from top to bottom after that 
        traverse right from bottom to top
        Postorder : traverse from left to right and from bottom to top
        Inorder  : traverse from left to right and from top to bottom
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key 
    
    # Traverse preoder
    def traversePreOrder(self):
        print(self.val, end= ' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInorder()
    
    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(11)
root.left.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInorder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()


