import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    queue = deque()

    for _ in range(n):
        comm = sys.stdin.readline().strip()

        if 'push_front' in comm:
            text, num = comm.split()
            queue.insert(0, int(num))
        elif 'push_back' in comm:
            text, num = comm.split()
            queue.append(int(num))
        elif comm == 'pop_front':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif comm == 'pop_back':
            if queue:
                print(queue.pop())
            else:
                print(-1)
        elif comm == 'size':
            print(len(queue))
        elif comm == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif comm == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif comm == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
