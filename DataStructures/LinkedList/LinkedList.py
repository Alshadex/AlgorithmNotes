'''
Linked lists is an ADT.

We will use two classes for our implmentation
 - Node: Allows us to string together elemnts of a list.
 -
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

	def prepend(self, value):
		''' Prepend Node with value to the beginning of self.'''
		if self.size == 0:
			self.size = 1
			self.front = Node(value)
			self.back = self.front
		else:
			new_node = Node(value)
			new_node.next = self.front
			self.front = new_node
			self.size += 1

	def length(self):
		return self.size

	def remove_front(self):
		''' Remove and return front node in Linked list '''
		if self.size == 0:
			raise LinkedListError('cannot remove from empty list')
		elif self.size == 1:
			value = self.front.value
			self.front = None
			self.back = None
			self.size = 0
			return value
		else:
			self.size -= 1
			value = self.front.value
			self.front = self.front.next
			return value

	def __getitem__(self, index):
		''' Return Node at given index in linked list '''
		n = self.front
		for i in range(index):
			n = n.next
		return n.value


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

	ll = LinkedList()
	for i in args.list:
		ll.append(i)
	print(ll)
	ll.remove_front()
	print(ll)
	ll.prepend(34)
	print(ll[2])