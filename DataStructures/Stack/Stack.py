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
