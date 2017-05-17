def main(n):
	'''
	A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
	Implement a method to count how many possible ways the child can run up the stairs
	'''
	if n <= 3:
		return n
	a, b, c, i  = 1, 2, 3, 4
	while i < n:
		a,b,c = b, c,a+b+c
		i += 1
	return a+b+c

if __name__ == '__main__':
	for i in range(10):
		print(main(i))

