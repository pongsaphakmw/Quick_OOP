class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def add_child(self, value, parent):
        new_node = Node(value)
        temp = self.root
        while temp is not None:
            if temp.value == parent:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("Parent not found")

    def print_tree(self):
        temp = self.root
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print_size(self):
        temp = self.root
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print(count)