import sys
import math
import numpy as np
import random

# Define the size of the memory
mem_size = 820000

# Calculate the height of the tree and the number of leaf nodes
height_tree = int(math.ceil(math.log(mem_size, 2)) - 1)
num_leaves = int(math.pow(2, height_tree))

# Create the main memory tree
main_mem_tree = [0] * int(math.pow(2, height_tree+1)-1)

# Initialize the main memory tree
for i in range(len(main_mem_tree)):
	main_mem_tree[i] = i

# Print the height and number of leaves in the tree
print("Tree height:", height_tree)
print("Number of leaves:", num_leaves)

# Define a function to get the path from a leaf node to the root node
def get_parents(tree_array, leaf_index):
	# Base case: If leaf index is 0, return an empty list
	if leaf_index == 0:
		return []

	# Calculate the index of the parent node
	parent_index = (leaf_index - 1) // 2

	# Recursively call the function to get the parent path
	parent_path = get_parents(tree_array, parent_index)

	# Append the parent node value to the path
	parent_path.append(tree_array[parent_index])

	# Return the parent path
	return parent_path

# Define functions to convert between leaf index and leaf address
def leaf_index_to_leaf_addr(leaf_index):
	return int(math.pow(2, height_tree-1)) + leaf_index + 1

def leaf_addr_to_leaf_index(leaf_addr):
	return leaf_addr - int(math.pow(2, height_tree-1)) - 1

# Define a function to find a leaf node for a given memory node index
def get_random_leaf_node(node):
	while (node <= int(math.pow(2, height_tree-1))):
		node = node*2 + random.randint(1, 2)
	return node

# Create a position map table for all memory nodes
position_map = []
for i in range(mem_size):
	position_map.append(leaf_addr_to_leaf_index(get_random_leaf_node(i)))

# Read input trace from file and write output trace to file
input_file = open("inputTrace.txt", "r")
output_file = open("outputTrace.txt", "w")
for line in input_file:
	data = line.split()
	node_addr = int(data[1])
	
	# Get the leaf node index for the memory node
	node_leaf_index = position_map[node_addr]
	
	
	
	# Get the path from the leaf node to the root node
	path = get_parents(main_mem_tree, leaf_index_to_leaf_addr(node_leaf_index))
	path.append(leaf_index_to_leaf_addr(node_leaf_index))
	
	# Updatee the position map with a random path
	position_map[node_addr] = leaf_addr_to_leaf_index(get_random_leaf_node(node_addr))
	
	# Write the "read" operations to the output trace file
	for i in range(len(path)):
		output_file.write("0 {}\n".format(int(path[i])))
	
	# Write the "write" operations to the output trace file
	for i in range(len(path)):
		output_file.write("1 {}\n".format(int(path[i])))
input_file.close()
output_file.close()

