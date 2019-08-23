# https://leetcode.com/problems/sort-array-by-parity/

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_index = 0
        odd_index = len(A)-1
           
        while even_index < odd_index:
            if A[even_index] % 2 == 0:
                even_index += 1
            else:
                tmp = A[even_index]
                A[even_index] = A[odd_index]
                A[odd_index] = tmp
                odd_index -= 1
        return A

# O(N) time complexity
# O(1) space complexity