from StacknQueue import *

class StackException(Exception):
        pass

def replace_ab(s):
        if len(s)<2:
                return s
        elif s[:2] == 'ab':
                return 'xy' + replace_ab(s[2:])
        else:
                return s[:2] + replace_ab(s[2:])


def contains(lst, value):
        if lst ==[]:
                return False
        for i in lst:
                if i == value:
                        return True
                elif isinstance(i, list):
                        return contains(i, value)
        return False


def skip_sum(n):
        if n == 0:
                return 0
        return n + skip_sum(n-1)


def swap_top(s):
        if not s.is_empty():
                temp = s.pop()
                if not s.is_empty():
                        temp2 = s.pop()
                        s.push(temp)
                        s.push(temp2)
                else:
                        raise StackException('BAD')
        else:
                raise StackException('BAAADDD')


def swap_bottom(s):
	t = Stack()

	while not s.is_empty():
		element = s.pop()
		t.push(element)

		while not s.is_empty():
			element2 = s.pop()

	s.push(element)
	t.pop()
	s.push(element2)

	while not t.is_empty():
		s.push(t.pop())

def duplicates(s):
	if s == '':
		return False
	elif len(s) == 1:
		return False
	elif s[:1] == s[1:2]:
		return True
	else:
		return duplicates(s[1:])