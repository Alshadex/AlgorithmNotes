from collections import deque


class BinaryTree:

	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def get_leaves(self):
		if self.leftChild == None and self.rightChild == None:
			return [self.key]
		if self.leftChild == None:
			return self.rightChild.get_leaves()
		if self.rightChild == None:
			return self.leftChild.get_leaves()
		return self.leftChild.get_leaves() + self.rightChild.get_leaves()

	def preorder(self):
		'''
		Root -> Left -> Right
		'''
		if self.leftChild == None and self.rightChild == None:
			return [self.key]
		if self.leftChild == None:
			return [self.key] + self.rightChild.preorder()
		if self.rightChild == None:
			return [self.key] + self.leftChild.preorder()
		return [self.key] + self.leftChild.preorder() + self.rightChild.preorder()

	def inorder(self):
		'''
		Left -> Root -> Right
		'''
		if self.leftChild == None and self.rightChild == None:
			return [self.key]
		if self.leftChild == None:
			return [self.key] + self.rightChild.inorder()
		if self.rightChild == None:
			return self.leftChild.inorder() + [self.key]
		return self.leftChild.inorder() + [self.key] + self.rightChild.inorder()

	def postorder(self):
		'''
		Left -> Right -> Root
		'''
		if self.leftChild == None and self.rightChild == None:
			return [self.key]
		if self.leftChild == None:
			return self.rightChild.postorder() + [self.key]
		if self.rightChild == None:
			return self.leftChild.postorder() + [self.key]
		return self.leftChild.postorder() + self.rightChild.postorder() + [self.key]


	def level_order(self):
		'''
		Breadth first search traversal
		'''
		q = deque()
		q.appendleft(self)
		while len(q) != 0:
			tmp = q.pop()
			if tmp.leftChild != None:
				q.appendleft(tmp.leftChild)
			if tmp.rightChild != None:
				q.appendleft(tmp.rightChild)
			print(tmp.key)


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

	t = BinaryTree(1)
	t.insertRight(3)
	t.insertLeft(4)
	t.insertLeft(2)
	t.leftChild.insertRight(5)
	print(t.get_leaves())
	print(t.inorder())
	print(t.postorder())
	print(t.preorder())
	print(t.level_order())

