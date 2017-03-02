#Longest common substring problem
from contextlib import contextmanager
from time import time
import re

@contextmanager
def time_it(name):
	start = time()
	yield
	print("Executed {} in {} seconds".format(name, time()-start))

def lcs(a, b):
	'''
	takes two strings a input 
	outputs the longest common substring
	'''
	temp = {}
	for i, x in enumerate(a):
		for j, y in enumerate(b):
			if x == y:
				temp[(i, j)] = temp.get((i-1, j-1), 0) + 1
	key = max(temp, key=temp.get)
	aindex = key[0]
	how_long = temp[key]
	return a[aindex-how_long+1 : aindex+1]

# def lcs_mine(a, b):
# 	# this is bad
# 	match = ''
# 	for i, x in enumerate(a):
# 		for y in re.finditer(x, b):
# 			temp = ''
# 			for c,d in zip(a[i:], b[y.start():]):
# 				if c == d:
# 					temp += c
# 			if len(temp) > len(match):
# 				match = temp
# 	return match

def test_lcs():
	ip_op_map ={
		('abc', 'bcd') : 'bc',
		('this is fun', 'function') : 'fun',
		('lorem ipo', 'ipo lorem') : 'lorem',
		('foo bar foo foo', 'foo foo bar') : 'foo bar',
		}
	for ip, op in ip_op_map.items():
		act = lcs(*ip)
		print("'{}'".format(op))
		print("'{}'".format(act))
		assert (op == act), 'exp : %s act : %s' % (op, act)

# def test_lcs_mine():
# 	ip_op_map ={
# 		('abc', 'bcd') : 'bc',
# 		('this is fun', 'function') : 'fun',
# 		('lorem ipo', 'ipo lorem') : 'lorem',
# 		('foo bar foo foo', 'foo foo bar') : 'foo bar',
# 		}
# 	for ip, op in ip_op_map.items():
# 		act = lcs_mine(*ip)
# 		assert (op == act), 'exp : %s act : %s' % (op, act)		

if __name__ == "__main__":
	# run_test
	#test_lcs()
	# test_lcs_mine()

	# performance
	#with time_it('LCS function : repeat : 1M'):
	#	for _ in range(1000000):
	#		lcs('abcdefgh', 'abcdefgh')

	# with time_it('LCS diff function : repeat : 1M'):
	# 	for _ in range(1000000):
	# 		lcs_mine('abcdefgh', 'abcdefgh')
	

	current_loc = (0,0)
	current_dir = (0,1)
	final_point = (2,2)

	change_dir = { 

	 (0,1):(1,0),
	 (1,0) : (0,-1),
	 (0, -1):(-1,0),
	 (-1,0):(0,1)

	}
	temp={(0,0):1}
	def next_loc(current_loc, current_dir):

		while current_loc != final_point :
			i,j = current_loc
			next_point = i+current_dir[0], j+current_dir[1]
			if 0<= next_point[0] <= 4 and 0<= next_point[1] <= 4 and not temp.get(next_point):
				current_loc = next_point
			else:
				current_dir = change_dir.get(current_dir) 
				current_loc =  i+current_dir[0], j+current_dir[1]
			print(current_loc)
			temp[current_loc] = 1

	print(next_loc((0,0), (0,1)))
