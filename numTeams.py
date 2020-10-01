############################################################################################################################
# File: evenGrandpas.py
# Author: Sam Wareing
# Description: my solution to LeetCode challenge 1315
# Challenge:  
# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
#
# Constraints: 
# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5
############################################################################################################################

def numTeams(rating): 
	teams = [] 

	numSoldiers = len(rating)

	for i in range(0, numSoldiers): 
		for j in range(i, numSoldiers): 
			for k in range(j, numSoldiers): 
				if (rating[k] < rating[j] and rating[j] < rating[i]) or (rating[k] > rating[j] and rating[j] > rating[i]): 
					teams.append((rating[i],rating[j],rating[k]))

	return teams

def runTest(input, output, testid):
	print("=========================================================")
	teams = numTeams(input)

	num_teams = len(teams) 

	print("teams: \t\t", teams)
	print("result: \t", num_teams)
	print("expected: \t", output)

	if num_teams == output: 
		result = "PASS"
	else: 
		result = "FAIL"

	print("TEST %d\t %s" % (testid, result))
	print("=========================================================")

if __name__ == '__main__': 
	# test 1 
	input = [2,5,3,4,1]
	output = 3
	runTest(input, output, 1)

	# test 2
	input = [2,1,3]
	output = 0
	runTest(input, output, 2)

	# test 3 
	input = [1,2,3,4]
	output = 4
	runTest(input, output, 3)









