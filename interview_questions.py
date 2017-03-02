import math 
from collections import Iterable
from operator import mul
from functools import reduce

def peak_finding_1d(iterable):
	pivot = len(iterable) // 2
	if pivot ==0 or iterable[pivot] >= iterable[pivot-1]:
		if pivot == len(iterable) -1 or iterable[pivot] >= iterable[pivot+1]:
			return iterable[pivot]
		else:
			return peak_finding_1d(iterable[pivot+1:])
	else:
		return peak_finding_1d(iterable[:pivot])

def peak_finding_2d(matrix):
	pass

def best_profit_stock_price(list_of_prices):
	max_profit = list_of_prices[1] - list_of_prices[0]
	low_price = list_of_prices[0]
	for current_price in list_of_prices:
		current_profit = current_price - low_price
		if current_profit > max_profit:
			max_profit = current_profit
		if current_price < low_price:
			low_price = current_price
	return max_profit

def min_no_of_squares(n):
	if n < 4:
		return n
	else:
		n = n - int(math.sqrt(n)) ** 2
		return 1 + min_no_of_squares(n)

def flatten_all(iterable):
	for i in iterable:
		if isinstance(i, Iterable) and not isinstance(i, str):
			yield from flatten_all(i)
		else:
			yield i 

def max_product_of_sub_array_of_k(k, iterable):
	max_product = reduce(mul, iterable[:k])
	current_product = max_product
	for i, x in enumerate(iterable[k:]):
		current_product = current_product * x / iterable[i]
		if current_product > max_product:
			max_product = current_product
	return max_product

def no_of_sub_array_with_sum_0(iterable):
	temp = {}
	_sum = 0
	zeroes = 0
	for x in iterable:
		_sum += x
		temp[_sum] = temp.get(_sum, 0) + 1
		if _sum == 0:
			temp[_sum] += 1
	return sum([v-1 for k,v in temp.items() if v > 1 ]) 

def lis(arr):
    one_before = None
    last = arr[0]
    count = 1
    for x in arr:
        print('x: {} last : {} one_before: {}'.format(x, last, one_before))
        if x >= last:
            one_before = last
            last = x
            count += 1
        elif one_before is None or one_before <= x <= last:
            last = x
    return count



if __name__ == "__main__":

	# peak finding 1d

	# assert peak_finding_1d(range(1000)) == 999 
	# assert peak_finding_1d(range(1000,1,-1)) == 1000
	# assert peak_finding_1d([1,2,3,4,3,2,1]) == 4

	# stock price
	# assert best_profit_stock_price(list(range(10))) == 9
	# assert best_profit_stock_price([5, 10, 3, 6]) == 5
	# assert best_profit_stock_price([5, 10, 3, 16]) == 13

	# min_no_of_squares
	# assert min_no_of_squares(25) == 1
	# assert min_no_of_squares(17) == 2
	# assert min_no_of_squares(3) == 3
	# assert min_no_of_squares(125) == 2

	# flatten_all
	# assert list(flatten_all([1,2,'3', 4])) == [1,2,'3', 4]
	# assert list(flatten_all([1,2,'34', 4, (1, '25', 3, )] )) == [1,2,'34', 4, 1, '25', 3]
	# assert list(flatten_all([1,2,'34', 4, (1, '25', 3, ), 5, 6, [4,]] )) == [1,2,'34', 4, 1, '25', 3, 5,6,4]

	# max_product_of_sub_array_of_k
	# assert max_product_of_sub_array_of_k(3, [10, 3, 4, 1, 7, 10]) == 120
	# assert max_product_of_sub_array_of_k(3, [10, 1, 4, 1, 5, 10]) == 50
	# assert max_product_of_sub_array_of_k(5, [10, 1, 4, 1, 5, 10]) == 200
	# assert max_product_of_sub_array_of_k(2, [10, 1, 4, 25, 5, 10]) == 125

	# no_of_sub_array_with_sum_0
	assert no_of_sub_array_with_sum_0([2,-2,3,4,0,-7,2,-2]) == 7 
	assert no_of_sub_array_with_sum_0([2,-2,3,4,0,-7,]) == 4
	assert no_of_sub_array_with_sum_0([2,-2,3,0,-7,4]) == 4
	assert no_of_sub_array_with_sum_0([2,-2,-3,0,-7,4]) == 2
	assert no_of_sub_array_with_sum_0([2,-2,-3,0,-7,4,0]) == 3
	assert no_of_sub_array_with_sum_0([0,0,0]) == 6




