class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def print_queue(self):
        temp = self.head
        while temp is not None:
            print('remaining queue is ', temp.value)
            temp = temp.next

    def is_empty(self):
        return self.head is None

    def print_size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print("queue's size ", count)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print_queue()
    print()
    queue.dequeue()
    queue.print_queue()
    print()
    queue.print_size()
    print()
    print('is queue empthy', queue.is_empty())
    print()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print('is queue empthy', queue.is_empty())
