def magic_index(arr):
	'''
	A magic index in an array A[ 0••• n -1] is de ned to be an index such that A[i] = i. 
	Given a sorted array of distinct integers, write a method to  nd a magic index, if one exists, in array A.
	'''
	low = 0
	high = len(arr)

	while low < high:
		mid = (low + high) // 2
		if arr[mid] == mid:
			return mid
		elif arr[mid] > mid:
			high = mid
		else:
			low = mid + 1
	return -1 



if __name__ == '__main__':

	arr = [-40,-20,-1,1,21,3,5,7,9,12,13]
	print(magic_index(arr))