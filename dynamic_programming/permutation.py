def permutation(s):
	'''
	Write a method to compute all permutations of a string of unique characters.
	'''
	n = len(s)
	if n == 1:
		return [s,]

	i = 0 
	res = []
	while i < n:
		for k in permutation(s[:i] + s[i+1:]):
			res.append(s[i] + k)			
		i += 1
	return res




if __name__ == '__main__':
	s = 'arun'
	print(permutation(s))