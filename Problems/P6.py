# 1. Import P5.py
# 2. Create a class called "PriorityQueue" that inherits from "Queue"
# 3. Create a method called "priority_enqueue" that adds a new node to the head of the queue
# 4. Create a method called "priority_dequeue" that removes the tail of the queue and returns the value of the removed node
# Use the methods to create a queue and manipulate (จัดการ) the queue from data2.txt
# Print the values of the queue

from P5 import Queue, Node
from checker import check_result

class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def priority_enqueue(self, value):
        pass
    
    def priority_dequeue(self):
        pass


if __name__ == '__main__':
    q = PriorityQueue()
    with open('data2.txt', 'r') as f:
        with open('data2_result.txt', 'w') as f2:
            for line in f:
                line = line.strip()
                if line.startswith('enqueue'):
                    q.enqueue(int(line.split()[1]))
                    f2.write(f'Enqueue {line.split()[1]}\n')
                elif line.startswith('dequeue'):
                    deq = q.dequeue()
                    f2.write(f'Dequeue {deq}\n')
                elif line.startswith('priority_enqueue'):
                    q.priority_enqueue(int(line.split()[1]))
                    f2.write(f'Priority enqueue {line.split()[1]}\n')
                elif line.startswith('priority_dequeue'):
                    prior_deq = q.priority_dequeue()
                    f2.write(f'Priority dequeue {prior_deq}\n')
        q.print_queue()
        print(q.is_empty())
        q.print_size()
    
    # Check the result
    check_result('data2_result.txt', 'data2_answer.txt')