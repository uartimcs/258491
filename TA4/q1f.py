#
# Binary Search Tree Printing Program (q1f.py)
#
# Purpose: This program makes use of the binarytree module of Python to draw a perfect binary search tree
# by carefully chosen integers as well as using bst function to automatically generate one.
# Then some basic properties of binary tree generated are shown in the console.
# 
# Limitations: The first binary tree requires the user to carefully choose a set of integers and add the nodes 
# sequentially. Otherwise, a unbalanced tree is resulted in.
# 
# Written by CHAN CHI HUNG (s12650050)
# On 02/05/2022
# For COMPS258 Assignment 4
#

# import Node, build, bst from building binary tree and BST.
from binarytree import Node, build, bst
# I don't use it, but it appears in skeleton file
import random
# ADD YOUR CODE HERE for (i)
# Refer to Activity 7.13

# Create a function insert for adding the number one-by-one
# Same level comparison
def insert(T, key):
    if T.val == key:
        print("Inserting a duplicate value is not allowed")
    elif key < T. val:
        if T.left:
            return insert(T.left, key)
        else:
            T.left = Node(key)
            return T
    else:
        if T.right:
            return insert(T.right, key)
        else:
            T.right = Node(key)
            return T

# The list is checked and arranged to make sure a perfect binary search tree can be built
# I have to make sure the items in the same level are arranged properly
# Otherwise, a unbalanced tree is resulted in.
dList = [68, 45, 87, 50, 37, 92, 76]
dTree = build([])

for num in dList:
    if dTree == None:
        dTree = Node(int(num))
    else:
        insert(dTree, int(num))
print("After adding:")
print(dTree)


# ADD YOUR CODE HERE for (ii)
# Height = 3, Perfect BST is required
# Create a perfect BST with height = 3 by bst module
root = bst(height = 3, is_perfect = True)
# Print the tree accordingly
print(root)

# ADD YOUR CODE HERE for (iii)
# Print the number of nodes , leaves, left most node and right most node to the console
print("The total number of nodes : ", root.size)
print("The total number of leaves : ", root.leaf_count)
print("The left most node in the tree : ", root.inorder[0].val)
print("The right most node in the tree : ", root.inorder[-1].val)
