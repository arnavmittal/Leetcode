# https://leetcode.com/problems/squares-of-a-sorted-array/

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        output_array = []
	    pos_index = 0

	    # Calculate positive number index
	    while pos_index < len(A) and A[pos_index] < 0:
	        pos_index += 1

	    # Calculate negative number index
	    neg_index = pos_index - 1

	    while neg_index >= 0 and pos_index < len(A):
	        if A[neg_index] ** 2 > A[pos_index] ** 2:
	            # Negative square bigger
	            output_array.append(A[pos_index] ** 2)
	            pos_index += 1
	        else:
	            # Positive square bigger
	            output_array.append(A[neg_index] ** 2)
	            neg_index -= 1

	    while pos_index < len(A):
	        # Add remaining squares of positive numbers
	        output_array.append(A[pos_index] ** 2)
	        pos_index += 1

	    while neg_index >= 0:
	        # Add remaining squares of negative numbers
	        output_array.append(A[neg_index] ** 2)
	        neg_index -= 1

	    return output_array

# O(N) time complexity
# O(N) space complexity