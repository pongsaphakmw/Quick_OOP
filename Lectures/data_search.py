class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Search:
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

    def search(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False


if __name__ == '__main__':
    s = Search()
    # Create a breadth-first search tree
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.insert(5)
    s.print_tree()
    print(s.search(3))