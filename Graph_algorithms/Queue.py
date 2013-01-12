from collections import deque

class Queue:
    def __init__(self,a):
        self.q = deque(a)

    def __str__(self):
        return str(self.q)
    
    def __len__(self):
        return len(self.q)

    def enqueue(self, a):
        self.q.append(a)

    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()
