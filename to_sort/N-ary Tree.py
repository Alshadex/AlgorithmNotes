class Tree:
  """Tree ADT; nodes may have any number of children"""

  def __init__(self: 'Tree',
               value: object =None, children: list =None):
    """Create node with value and any number of children"""

    self.value = value
    if children == None:
      self.children = []
    else:
      self.children = children[:] 

  def __repr__(self: 'Tree') -> str:
    """Return representation of Tree as a string"""
    return ('Tree(' + repr(self.value) + ', ' +
            repr(self.children) + ')')



def arity(t: Tree) -> int:
  """Return maximum branching factor of t

  >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
  >>> tn3 = Tree(3, [Tree(6), Tree(7)])
  >>> tn1 = Tree(1, [tn2, tn3])
  >>> arity(tn1)
  4
  """
  if t.children == []:
    return 0
  maximum = len(t.children)
  for child in t.children:
    if arity(child) > maximum:
      maximum = arity(child)
  return maximum


def count(t: Tree) -> int:
  """Return number of nodes in t

  >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
  >>> tn3 = Tree(3, [Tree(6), Tree(7)])
  >>> tn1 = Tree(1, [tn2, tn3])
  >>> count(tn1)
  9
  """
  total = 1
  for child in t.children:
    total = total + count(child)
  return total
  

def height(t: Tree) -> int:
  """Return length of longest path of t

  >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
  >>> tn3 = Tree(3, [Tree(6), Tree(7)])
  >>> tn1 = Tree(1, [tn2, tn3])
  >>> height(tn1)
  2
  """
  if t.children == []:
    return 0
  tallest = 0
  for child in t.children:
    tallest = max(tallest, height(child))
  return tallest + 1


def leaf_count(t: Tree) -> int:
  """Return number of leaves in t

  >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
  >>> tn3 = Tree(3, [Tree(6), Tree(7)])
  >>> tn1 = Tree(1, [tn2, tn3])
  >>> leaf_count(tn1)
  6
  """
  if not t.children:
    return 1
  total = 0
  for child in t.children:
    total = total + leaf_count(child)
  return total
