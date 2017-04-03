class Node(object):
	def __init__(self, value, _next=None):
		self.value = value
		self._next = _next

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self, *args):
		self.head = None
		for val in args[::-1]:
			self.head = Node(val, self.head)

	def insert(self, pos, val):
		if pos == 0:
			self.head = Node(val, self.head)
			return True

		curr = self.head
		while curr and curr._next and pos >= 1:
			pos -= 1
			curr = curr._next
		if pos == 0 and curr:
			curr._next = Node(val, curr._next)
			return True
		return False

	def __str__(self):
		curr = self.head
		s = ''
		while curr:
			s += str(curr.value) + ' --> '
			curr =  curr._next
		return s[:-5

def addnodes(n1, n2):
	tot = n1.value + n2.value
	carry = tot % 10
	tot = tot / 10
	return tot, carry


def adding_two_numbers_reverse_order(n1, n2):
	n1node = n1.head
	n2node = n2.head
	ret = LinkedList()
	while (n1node or n2node):
		tot, carry = addnodes(n1node, n2node)

def 




if __name__ == "__main__":




