############################################################################################################################
# File: bst_to_gst.py
# Author: Sam Wareing
# Description: my solution to LeetCode challenge 1038 
# Challenge:  
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original 
# BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val <= 100
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
############################################################################################################################

class Node:
    def __init__(self, data=None, **kwargs):
        self.data = data
        self.left = None
        self.right = None

        if 'inputs' in kwargs.keys():
            for val in kwargs['inputs']:
                self.insert(val)
        

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

    # Function to return level order of tree as an array 
    def getLevelOrder(self): 
        treeArray = [] 
        h = Node.__height(self) 
        for i in range(1, h+1): 
            treeArray += Node.__addGivenLevel(self, i)
        return treeArray
      
      
    # add node to array 
    def __addGivenLevel(root, level): 
        treeArray = [] 
        if root is None: 
            treeArray+=[None]
            return treeArray

        if level == 1: 
            treeArray+=[root.data]
            return treeArray
        elif level > 1 : 
            #print(root.data)
            treeArray += Node.__addGivenLevel(root.left , level-1)
            treeArray += Node.__addGivenLevel(root.right , level-1)
            return treeArray
      
      
    """ Compute the height of a tree--the number of nodes 
        along the longest path from the root node down to 
        the farthest leaf node 
    """
    def __height(node): 
        if node is None: 
            return 0 
        else : 
            # Compute the height of each subtree 
            lheight = Node.__height(node.left) 
            rheight = Node.__height(node.right) 
      
            # Use the larger one 
            if lheight > rheight: 
                return lheight+1
            else: 
                return rheight+1

# function to convert a BST to a GST
def greaterTree(root):
    global sum
    if root: 
        greaterTree(root.right)
        sum+=root.data
        root.data = sum 
        greaterTree(root.left)
    else:
        return 0

def runTest(inputs, output, testid): 
    global sum
    sum = 0

    binTree = Node(inputs=inputs)
    initial = binTree.getLevelOrder()
    greaterTree(binTree)
    results = binTree.getLevelOrder()

    if output == results:
        print("Test %d\tPASS" % testid)
    else:
        print("Test %d\tFAIL" % testid)

    print("initial: \t", initial)
    print("expected: \t", output)
    print("actual: \t", results)
    



if __name__ == "__main__":
    # test 1 
    inputs = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    output = [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
    runTest(inputs, output, 1)

    # test 2 
    inputs = [0,1]
    output = [1,None,1]
    runTest(inputs, output, 2)

    # test 3
    inputs = [1,0,2]
    output = [3,3,2]
    runTest(inputs, output, 3)

    # test 4
    inputs = [3,2,4,1]
    output = [7,9,4,10]
    runTest(inputs, output, 4)    










