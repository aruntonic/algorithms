def multiply(a, b):
	'''
	Write a recursive function to multiply two positive integers without using the *operator.
	You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
	'''
	res = 0
	i = 0 
	while b:
		if b & 1:
			res += a << i
		b >>= 1
		i += 1
	return res


if __name__ == '__main__':
	print(multiply(25, 35))