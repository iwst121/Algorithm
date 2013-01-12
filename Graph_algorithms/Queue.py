from collections import deque

class Queue:
    """
        This class wraps the system defined deque to make it behaves like a
        queue.
    """
    def __init__(self,a):
        self.q = deque(a)

    def __str__(self):
        return str(self.q)
    
    def __len__(self):
        return len(self.q)

    def enqueue(self, a):
        self.q.append(a)

    def dequeue(self):
        return self.q.popleft()
