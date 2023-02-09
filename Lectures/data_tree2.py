class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def print_tree(self):
        def print_tree_helper(node, level):
            print('-' * level + str(node.data))
            if node.left:
                print_tree_helper(node.left, level + 1)
            if node.right:
                print_tree_helper(node.right, level + 1)
        print_tree_helper(self.root, 0)

    def add_node(self, val):
        def add_node_helper(node, val):
            if val < node.data:
                if node.left:
                    add_node_helper(node.left, val)
                else:
                    node.left = Node(val)
            else:
                if node.right:
                    add_node_helper(node.right, val)
                else:
                    node.right = Node(val)
        add_node_helper(self.root, val)


if __name__ == '__main__':
    root = Node(8)
    tree = Tree(root)
    tree.add_node(3)
    tree.add_node(10)
    tree.add_node(1)
    tree.add_node(6)
    tree.add_node(14)
    tree.add_node(4)
    tree.add_node(7)
    tree.print_tree()
