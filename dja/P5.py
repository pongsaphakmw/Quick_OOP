# 1. Create a parent class call "Node" with "value" and "next" attributes
# 2. Create a child class call "Queue" with "head" and "tail" attributes
# 3. Create a method called "enqueue" that adds a new node to the tail of the queue
# 4. Create a method called "dequeue" that removes the head of the queue and returns the value of the removed node
# 5. Create a method called "print_queue" that prints the values of the queue
# 6. Create a method called "is_empty" that returns True if the queue is empty and False otherwise
# 7. Create a method called "print_size" that prints the size of the queue
# Use the methods to create a queue and manipulate (จัดการ) the queue from data.txt
# Print the values of the queue
# ข้อนี้ทำให้เพราะยากชิบหาย

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
        # q.print_size() Use this to print the size of the queue
    print(f'Is queue empty: {q.is_empty()}')
    # q.print_queue()