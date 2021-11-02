'''
push uses append, and pop uses pop(), append and pop use constant-time.

We already know that append() is constant-time,
but pop(0) is slower (linear - time) because after deleting index 0, 
all the other elements have to be moved one place forward.
'''


class Stack:
    def __init__(self):
        self._data = []

    def push(self, o):
        self._data.append(o)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0
        # or return self._data = []

'''
We already know that append() is constant-time,
but pop(0) is slower (linear - time) because after deleting index 0, 
all the other elements have to be moved one place forward.

same thing with using insert(0)
'''

class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, o):
        self._data.insert(0, o)

    def dequeue(self):
        return self._data.pop()

    def front(self):
        return self._data[len(self._data)-1]

    def is_empty(self):
        return len(self._data) == 0
        # or return self._data = []