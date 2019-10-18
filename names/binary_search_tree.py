import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
#from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.counter = 0
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    
    def insert(self, value):
      
        # For empty trees
        if self.left == None and value < self.value:
            self.left = BinarySearchTree(value)
            
        if self.right == None and value > self.value:
            self.right = BinarySearchTree(value)
            
        # Recursion Examples
        if self.left and value < self.value:
            self.left.insert(value)
            
        if self.right and value > self.value:
            self.right.insert(value)
        
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.left and target < self.value:
                return self.left.contains(target)
            elif self.right and target > self.value:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        self.value = cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        else:
            return self

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):   
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        queue = Queue()
        queue.enqueue(self)
        
        while queue.size > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        
        while stack.size > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass