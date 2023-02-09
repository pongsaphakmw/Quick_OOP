# Create a class "Node" that use for creating a node in a tree
# The node should have 2 attributes: "data" and "children"
# Create a class "Tree" that use for creating a tree


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return self.data


class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        def print_tree_helper(node, level):
            print('-' * level + node.data)
            for child in node.children:
                print_tree_helper(child, level + 1)

        print_tree_helper(self.root, 0)


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
