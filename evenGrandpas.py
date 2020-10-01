############################################################################################################################
# File: evenGrandpas.py
# Author: Sam Wareing
# Description: my solution to LeetCode challenge 1315
# Challenge:  
#
# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
# (A grandparent of a node is the parent of its parent, if it exists.)
# If there are no nodes with an even-valued grandparent, return 0
# 
#Constraints:
#
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
############################################################################################################################

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, leftData, rightData): 
     	if leftData:
     		self.left = Node(leftData)
     	else:
     		self.left = None

     	if rightData: 
     		self.right = Node(rightData)
     	else: 
     		self.right = None


def sumEvenGrandpas(root): 
	global sum 
	if root:
		print(root.data)
		if (root.data % 2 == 0): 	# if current node is even, find it's "grandchildren"
			# sum values of grandchildren on left side
			child = root.left
			if child:
				if child.left:
					sum+=child.left.data
				if child.right:
					sum+=child.right.data 

			# sum values of grandchildren on right side
			child = root.right
			if child:
				if child.left:
					sum+=child.left.data
				if child.right:
					sum+=child.right.data 

		sumEvenGrandpas(root.left) 
		sumEvenGrandpas(root.right) 

	return sum




def runTest(inputs, output, testid): 
	global sum 
	sum = 0 

	# I cannot figure out how to do this part dynamicaly :( 
	binTree = Node(6)
	binTree.insert(7,8)
	nextNode = binTree.left 
	nextNode.insert(2,7) 
	nextNode = binTree.right 
	nextNode.insert(1,3)
	nextNode = binTree.left.left
	nextNode.insert(9, None)
	nextNode = binTree.left.right 
	nextNode.insert(1,4) 
	nextNode = binTree.right.left
	nextNode.insert(None, None) 
	nextNode = binTree.right.right 
	nextNode.insert(None, 5)

	print(sumEvenGrandpas(binTree))


    



if __name__ == "__main__":
    # test 1 
    inputs = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    output = 18
    runTest(inputs, output, 1)