############################################################################################################################
# File: diagSortMat.py
# Author: Sam Wareing
# Description: my solution to LeetCode challenge 1329
# Challenge:  
# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then 
# return the sorted array.
############################################################################################################################

def sortDiagonally(matrix): 

	# determine dimensions of matrix 
	num_rows = len(matrix) 
	num_cols = len(matrix[0])

	# store diagonals into dictionary, key = (m,n) where diag starts 
	diagonals = {} 

	# add diagonals starting at row 0 
	for n in range(0, num_cols):
			diagonals[(0,n)] = [matrix[0][n]]
			i = 1
			j = n + 1
			while i < num_rows and j < num_cols: 
				diagonals[(0,n)].append(matrix[i][j])
				i+=1
				j+=1
	# add diagonals starting at col 0 (minus row 0)
	for m in range(1, num_rows):
			diagonals[(m,0)] = [matrix[m][0]]
			i = m + 1 
			j = 1
			while i < num_rows and j < num_cols: 
				diagonals[(m,0)].append(matrix[i][j])
				i+=1
				j+=1
	
	for diag in diagonals.keys(): 
		m, n = diag
		sortedDiag = sorted(diagonals[diag])
		for val in sortedDiag: 
			matrix[m][n] = val
			m+=1 
			n+=1



		
	return matrix



def runTest(input, output, testid): 
	result = sortDiagonally(input)
	print(result)


if __name__ == '__main__': 
	# test 1
	input = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
	output = [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
	runTest(input, output, 1)