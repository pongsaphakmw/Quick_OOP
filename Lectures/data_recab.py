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
            print(temp.value)
            temp = temp.next

    def is_empty(self):
        return self.head is None

    def print_size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print(count)

if __name__ == '__main__':
    q = Queue()
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.strip()
            node_val = int(line.split(' ')[1])
            if line.startswith('enqueue'):
                q.enqueue(int(line.split(' ')[1]))
                print(f'Enqueue {node_val} to queue')
            elif line.startswith('dequeue'):
                deq = q.dequeue()
                print(f'Dequeue {deq} from queue')