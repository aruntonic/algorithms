def powerset(arr):
	'''
	Write a method to return all subsets of a set.
	'''
	result = []
	n = 2 ** len(arr)
	i = 0
	l = len(arr) - 1

	while i < n:
		s = []
		j = l
		k = i
		while k:
			if k  & 1:
				s.append(arr[j])
			k >>= 1
			j -=1 
		result.append(s)
		i += 1
	return result 

if __name__ == '__main__':
	arr = [1,2,3,4]
	print(powerset(arr))