from random import randint

def rand_queue(file_name):
    with open(file_name, 'w') as f:
        for i in range(200):
            num = randint(1, 255)
            if i % 2 == 0:
                f.write(f'enqueue {num}\n')
            else:
                f.write(f'dequeue {num}\n')

def rand_priority_queue(file_name):
    with open(file_name, 'a') as f:
        for i in range(200):
            num = randint(1, 255)
            if i % 2 == 0:
                f.write(f'priority_enqueue {num}\n')
            else:
                f.write(f'priority_dequeue {num}\n')

if __name__ == '__main__':
    rand_queue('data.txt')
    rand_queue('data2.txt')
    rand_priority_queue('data2.txt')