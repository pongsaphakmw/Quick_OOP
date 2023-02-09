from random import randint
import time
import sys

sys.setrecursionlimit(150000)


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root

    def add_node(self, value):
        def add_node_helper(node, value):
            if value < node.value:
                if node.left:
                    add_node_helper(node.left, value)
                else:
                    node.left = Node(value, node)
            else:
                if node.right:
                    add_node_helper(node.right, value)
                else:
                    node.right = Node(value, node)

        add_node_helper(self.root, value)

    def print_tree(self):
        def print_tree_helper(node, level):
            print('-' * level + str(node.value))
            if node.left:
                print_tree_helper(node.left, level + 1)
            if node.right:
                print_tree_helper(node.right, level + 1)

        print_tree_helper(self.root, 0)

    def find_node(self, value):
        def find_node_helper(node, value):
            if node.value == value:
                return node
            elif value < node.value:
                if node.left:
                    return find_node_helper(node.left, value)
                else:
                    return None
            else:
                if node.right:
                    return find_node_helper(node.right, value)
                else:
                    return None

        return find_node_helper(self.root, value)

    def delete_node(self, value):
        node = self.find_node(value)
        if node:
            if node.left is None and node.right is None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            elif node.left is None:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            elif node.right is None:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.value = min_node.value
                if min_node.parent.left == min_node:
                    min_node.parent.left = min_node.right
                else:
                    min_node.parent.right = min_node.right

    def breadth_first_search(self, value):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def linear_search(self, value):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def binary_search(self, value):
        def binary_search_helper(node, value):
            if node.value == value:
                return True
            elif value < node.value:
                if node.left:
                    return binary_search_helper(node.left, value)
                else:
                    return False
            else:
                if node.right:
                    return binary_search_helper(node.right, value)
                else:
                    return False

        return binary_search_helper(self.root, value)


if __name__ == '__main__':
    root = Node(8)
    tree = Tree(root)
    max_case = 10000
    for i in range(max_case):
        tree.add_node(randint(i, i+100))
    # tree.print_tree()
    test_case = randint(0, max_case)
    bfs_start_time = time.time()
    print('Breadth first search starting time', bfs_start_time)
    print(tree.breadth_first_search(test_case))
    bfs_end_time = time.time()
    print('Breadth first search ending time', bfs_end_time)
    print('Breadth first search average time', bfs_end_time-bfs_start_time)
    ls_start_time = time.time()
    print('Linear search starting time', ls_start_time)
    print(tree.linear_search(test_case))
    ls_end_time = time.time()
    print('Linear search ending time', ls_end_time)
    print('Linear search average time', ls_end_time-ls_start_time)
    bs_start_time = time.time()
    print('Binary search starting time', bs_start_time)
    print(tree.binary_search(test_case))
    bs_end_time = time.time()
    print('Binary search ending time', bs_end_time)
    print('Binary search average time', bs_end_time-bs_start_time)
