############################################################################################################################
# File: evenGrandpas.py
# Author: Sam Wareing
# Description: a simple BFS
############################################################################################################################

import queue

class Node: 
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data): 
		if not(data is None):
			if self.data is None: 
				self.data = data
			else:
				if data < self.data:
					if self.left is None:
						self.left = Node(data)
					else:
						self.left.insert(data)
				elif data > self.data:
					if self.right is None:
						self.right = Node(data)
					else:
						self.right.insert(data)


def print_bfs(root): 
	Q = queue.Queue()
	Q.put(root)

	while not(Q.empty()):
		s = Q.get(0)

		if s: 
			print(s.data, end=" ")
			if s.left: 
				Q.put(s.left)
			else:
				Q.put(None)
			if s.right: 
				Q.put(s.right)
			else:
				Q.put(None)
		else:
			print(None, end=" ")





def runTest(inputs): 

	root = Node(None)

	for data in inputs: 
		root.insert(data)

	print_bfs(root)




if __name__ == '__main__':
	inputs = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
	runTest(inputs)









