#Excercise 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        if data == None:
            self.head = None
        else:
            self.head = Node(data)

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        current = self.head
        my_string = ""
        while current:
            #print(current.data, end=" -> ")
            my_string += f"{current.data} -> "
            current = current.next
        my_string += "None"
        return my_string
    
    def retrieve_x_node(self,index):
        current = self.head
        for i in range(index):
            current = current.next
            if not current:
                raise IndexError("index out of range")
        return current
    
    def Cycle(self):
        p1=self.head
        p2=self.head

        while p1 :
            while p2 :
                if p2.next == p1 :
                    return True
                
                p2 = p2.next
            p1 = p1.next

        return False
    

#Excercise 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
    
        def delete(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                self.delete_node(node)
                return
            node = node.next
    
     def reverse(self):
        current = self.head
        temp = None
        
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev


#Excercise 3
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = TreeNode(root) if root else None
    
    def postorder_traversal(self, root):
        values = []
        if root:
            values = self.postorder_traversal(root.left)
            values = values + self.postorder_traversal(root.right)
            values.append(root.val)
        return values
