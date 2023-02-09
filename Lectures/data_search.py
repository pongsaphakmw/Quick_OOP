class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return self.data


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []


class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        def print_tree_helper(node, level):
            print('-' * level + node.data)
            for child in node.children:
                print_tree_helper(child, level + 1)

        print_tree_helper(self.root, 0)

    def breadth_first_search(self, val):
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.data == val:
                return node
            for child in node.children:
                queue.enqueue(child)
        return None


if __name__ == '__main__':
    root = Node('Electronics')
    laptop = Node('Laptop')
    laptop.add_child(Node('Macbook'))
    laptop.add_child(Node('Surface'))
    laptop.add_child(Node('Thinkpad'))
    tv = Node('TV')
    tv.add_child(Node('Samsung'))
    tv.add_child(Node('LG'))
    tv.add_child(Node('Sony'))
    root.add_child(laptop)
    root.add_child(tv)
    tree = Tree(root)
    tree.print_tree()
    print(tree.breadth_first_search('Thinkpad'))
    print(tree.breadth_first_search('iPhone'))
    print(tree.breadth_first_search('LG'))
    print(tree.breadth_first_search('Macbook'))
