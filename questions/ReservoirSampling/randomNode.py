import random

'''
Reservoir Sampling is a way to choose k items from a sample of items
where the size of the sample is unknown.

Reservoir sampling goes through every single item, counting them
and reduces the probability slightly of choosing them.

The probability of choosing every item is equal. 
This example makes use of my linked list implemenation.
'''
class Node:
	def __init__(self, value, next: 'Node' = None):
		self.value = value
		self.next = next

	def __repr__(self):
		if not self.next:
			return 'Node({})'.format(repr(self.value))
		else:
			return 'Node({}, {})'.format(repr(self.value), repr(self.next))

class LinkedList:
	''' Collection of Nodes to form a linked list'''

	def __init__(self) -> None:
		self.front = None
		self.back = None
		self.size = 0

	def __repr__(self):
		return 'LinkedList({})'.format(self.front)

	def append(self, value):
		if self.size == 0:
			new_node = Node(value)
			self.size = 1
			self.front = new_node
			self.back = new_node
		else:
			self.size += 1
			new_node = Node(value)
			self.back.next = new_node
			self.back = new_node


def getRandom(head: Node) -> int:
    '''
    Implemenation of reservoir sampling known as Algorithm R.
    Notice that the linked list's size is never used.
    '''
    chosen_val = 0
    curr = head
    scope = 1
    
    while curr:
        if random.random() < 1/scope:
            chosen_val = curr.value
        curr = curr.next
        scope +=1
    
    return chosen_val


if __name__ == "__main__":
    import argparse
    CLI=argparse.ArgumentParser()
    CLI.add_argument(
        "--list",
        nargs="*",
        type=int,
        default=[3,2,1]
    )
    args = CLI.parse_args()

    print(f'Array: {args.list}')
    linked_lst = LinkedList()
    for i in args.list:
        linked_lst.append(i)
    Sorted = getRandom(linked_lst.front)
    print(f'Result: {Sorted}')
