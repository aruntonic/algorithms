def tower_of_hanoi(n, source, buffer, dest):
	'''
	In the classic problem of the  wers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. 
	The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).You have the following constraints:
	(1) Only one disk can be moved at a time.
	(2) A disk is slid off the top of one tower onto another tower.
	(3) A disk cannot be placed on top of a smaller disk.
	Write a program to move the disks from the first tower to the last using stacks.
	'''

	if n <= 0 :
		return

	tower_of_hanoi(n-1, source, dest, buffer)
	dest.append(source.pop())
	tower_of_hanoi(n-1, buffer, source, dest)

if __name__ == '__main__':

	source = [5, 4, 3, 2, 1]
	buffer = []
	dest = []

	print(source, buffer, dest)
	tower_of_hanoi(5, source, buffer, dest)
	print(source, buffer, dest)

