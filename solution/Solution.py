# This is the definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Initialize a variable to store the count of valid pairs
        self.res = 0

        # Define a helper function to solve the problem
        def solve(root):
            # If the root is None, return an empty dictionary
            if root is None:
                return {}
            
            # If the root is a leaf node, return a dictionary with 1 as the key and 1 as the value
            if root.left is None and root.right is None:
                # This means we have a leaf node here
                return {1: 1}
            
            # Recursively call the solve function on the left and right children of the root
            lhNodes = solve(root.left)            
            rhNodes = solve(root.right)
            
            # Iterate over the heights of the left and right subtrees
            for leftNodeHeight in lhNodes:
                for rightNodeHeight in rhNodes:
                    # If the sum of the heights is less than or equal to the distance, increment the result
                    if leftNodeHeight + rightNodeHeight <= distance:
                        self.res += lhNodes[leftNodeHeight] * rhNodes[rightNodeHeight]

            # Create a new dictionary to store the heights of the nodes in the current subtree
            nhNodes = {}
            # Iterate over the heights of the left subtree
            for key in lhNodes:
                # If the height is less than or equal to the distance, add it to the new dictionary
                if key <= distance:
                    nhNodes[key + 1] = lhNodes[key]
            # Iterate over the heights of the right subtree
            for key in rhNodes:
                # If the height is less than or equal to the distance, add it to the new dictionary
                if key <= distance:
                    nhNodes[key + 1] = nhNodes.get(key + 1, 0) + rhNodes[key]
            
            # Return the new dictionary
            return nhNodes

        # Call the solve function on the root of the tree
        solve(root)
        # Return the result
        return self.res