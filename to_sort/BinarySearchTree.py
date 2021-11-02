class BTNode:
    def __init__(self, data, left=None, right=None):
    	self.data = data
    	self.left = left
    	self.right = right

    def __repr__(self):
    	return ('BTNode(' + str(self.data) + ', ' + repr(self.left) +
            ', ' + repr(self.right) + ')')

    def is_leaf(self):
    	return not self.left and not self.right


class BST:
    """Binary search tree."""

    def __init__(self: 'BST', root: BTNode=None) -> None:
        """Create BST with BTNode root."""
        self._root = root

    def __repr__(self: 'BST') -> str:
        """Represent this binary search tree."""
        return 'BST(' + repr(self._root) + ')'

    def insert(self: 'BST', data: object) -> None:
        """Insert data, if necessary, into this tree.

        >>> b = BST()
        >>> b.insert(8)
        >>> b.insert(4)
        >>> b.insert(2)
        >>> b.insert(6)
        >>> b.insert(12)
        >>> b.insert(14)
        >>> b.insert(10)
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(12, BTNode(10, None, None), BTNode(14, None, None))))
    """
        self._root = _insert(self._root, data)

    def find(self: 'BST', data: object) -> BTNode:
        """Return node containing data, otherwise return None."""
        return _find(self._root, data)

    def delete(self: 'BST', data: object) -> None:
        """Remove, if present, node containing data.

        >>> b = BST()
        >>> b.insert(8)
        >>> b.insert(4)
        >>> b.insert(2)
        >>> b.insert(6)
        >>> b.insert(12)
        >>> b.insert(14)
        >>> b.insert(10)
        >>> b.delete(12)
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(10, None, BTNode(14, None, None))))
        >>> b.delete(14)
        >>> b
        BST(BTNode(8, BTNode(4, BTNode(2, None, None), BTNode(6, None, None)),\
 BTNode(10, None, None)))
        """
        self._root = _delete(self._root, data)

    def height(self: 'BST') -> int:
        """Return height of this tree."""
        return _height(self._root)



def _find(node: BTNode, data: object):
    """Return the node containing data, or else None."""
    if not node or node.data == data:
        return node
    else:
        return (_find(node.left, data) if data < node.data
                else _find(node.right, data))

def _insert(node: BTNode, data: object) -> BTNode:
    """Insert data in BST rooted at node,
       and return root.
    """
    return_node = node
    if node is None:
        return_node = BTNode(data)
    elif data < node.data:
        node.left = _insert(node.left, data)
    elif data > node.data:
        node.right = _insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node

def _find_max(node: BTNode) -> BTNode:
    """Find and return maximal node, assume node is not None
    """
    if node.right == None:
        return node
    return _find_max(node.right)

def _find_max_iter(node: BTNode) -> BTNode:
    """The iterative implementation of find_max, i.e., not using recursion
    """
    while node.right != None:
        node = node.right
    return node


def _delete(node: BTNode, data: object) -> BTNode:
    """Delete, if exists, node with data and return resulting tree."""
    # Algorithm for _delete:
    # 1. If this node is None, return that
    # 2. If data is less than node.data, delete it from left child and
    #     return this node
    # 3. If data is more than node.data, delete it from right child
    #     and return this node
    # 4. If node with data has fewer than two children,
    #     and one is None, return the other one
    # 5. If node with data has two non-None children,
    #     replace data with that of its largest child in the left subtree (the predecessor),
    #     now temporarily you have two nodes with the predecessor's data,
    #     delete the predecessor node in the left subtree, and return this node
    return_node = node
    if node == None:
        pass
    elif data < node.data:
        node.left = _delete(node.left, data)
    elif data > node.data:
        node.right = _delete(node.right, data)
    elif node.left == None:  # node.data == data and node has no left child (could be no child at all)
        return_node = node.right
    elif node.right == None: # node.data == data and node has a single left child
        return_node = node.left
    else:   # node.data == data and node has both children
        node.data = _find_max(node.left).data  
        node.left = _delete(node.left, node.data) 
    return return_node

def _height(node: BTNode) -> int:
    """Return height of tree rooted at node."""
    return 1 + max(_height(node.left), _height(node.right)) if node else -1
