def binary_tree(value):
	return [value, None, None]

def insert_left(bt, value):
	if bt == None:
		raise ValueError('cannot insert into empty tree')
	left_branch = bt.pop(1)
	bt.insert(1, [value, left_branch, None])

def insert_right(bt, value):
	if bt == None:
		raise ValueError('cannot insert into empty tree')
	right_branch = bt.pop(2)
	bt.insert(2, [value, None, right_branch])

def height(bt):
	if bt == None:
		return 0
	return 1 + max(height(bt[1]), height(bt[2]))

def contains(bt, value):
	if bt == None:
		raise ValueError()
	return bt[0] == value or contains(bt[1], value) or contains(bt[2], value)

def preorder(bt):
	if bt == None:
		return []
	return [bt[0]] + preorder(bt[1]) + preorder(bt[2])



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
		if self.leftChild == None and self.rightChild == None:
                        return [self.key]
		if self.leftChild == None:
			return self.rightChild.preorder()
		if self.rightChild == None:
			return self.leftChild.preorder()
		return self.leftChild.preorder() + self.rightChild.preorder()
def expr(tree):
	if not tree:
		return ''
	s = '(' + expr(tree.leftChild)
	s = s + str(tree.key)
	s = s + expr(tree.rightChild) + ')'
	return s
