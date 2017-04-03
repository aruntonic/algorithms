import random

def _max_2(a, b):
	return a if a >= b else b 

def best_pick(b):
	if len(b) <= 3:
		return max(b)
	else:
		pass




	# a1 = b[0]
	# a2 = b[-1]

	# b1 = b[1],b[-1]
	# b2 = b[0],b[-2] 

toss = lambda : round(random.random())

def display_board(b):
	print(b)

def display_pick(p, i):
	player = 'Computer' if p else 'You'
	print('{} picks {}')

def findRotateSteps(nums, k):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """
    t = {}
    count = 0
    pairs = {}
    for i in sorted(nums):
        j = t.get(i)
        if j is not None:
            count += 1
            pairs[(i,j)] = True
            del t[i]
        if (i+k, i) not in pairs:
            t[i+k] = i
        print(t)
        print(pairs)

    return count
       

if __name__ == '__main__':
	# board = [random.randint(1,100) for _ in random.randint(1, 10)]
	# display_board(b)
	# if toss():
	# 	print('Computer wins the toss and takes the first pick')

	findRotateSteps([1,2,3,4,5], -1)
		

	# while(b):





	
