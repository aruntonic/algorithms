def main(grid):
	'''
	Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
	The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. 
	Design an algorithm to find a path for the robot from the top left to the bottom right.
	'''

	start = (0,0)
	end = (len(grid) -1, len(grid[0]) - 1)
	cache = {}

	path = []

	recursion(end, grid, cache, path)
	return path

def isStart(x, y):
	return x == 0 and y ==0 

def moveUp(x,y):
	return x, y - 1

def moveLeft(x, y):
	return x - 1, y

def outOfTheBox(x,y):
	return x < 0  or y < 0

def blockedCell(coord, grid):
	x, y = coord
	return not grid[x][y]

def recursion(coord, grid, cache, path):
	# print(coord)
	if outOfTheBox(*coord) or blockedCell(coord, grid):
		return False

	cache_path = cache.get(coord, [])
	if cache_path:
		path.extend(cache_path)
		print(coord)
		return True

	if isStart(*coord) or recursion(moveUp(*coord), grid, cache, path) or recursion(moveLeft(*coord), grid, cache, path):
		path.append(coord)
		cache[coord] = path
		return True

if __name__ == '__main__':

	grid = [
	[True, True, False],
	[True, True, True],
	[True, False, True],
	[False, True, True],
	]
	print(main(grid))
