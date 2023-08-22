class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        i = 0
        j = 1
        while i < len(nums) - 1:
            if nums[i] == nums[j]:
                good_pairs += 1
            j += 1
            if j == len(nums):
                i += 1
                j = i + 1
        return good_pairs
        







'''
Problem

Navigate through an array an return the number of good pairs (i and j). Good pairs meaning that the values of i and j are identical and i < j.
'''

'''
Solution 

Create a while loop that runs as long as i < len(nums) - 1:
This way we know the loop wont end until each value has been checked. Check each value using the j pointer once j reaches
the end increment i since we know that each value at that index is checked and set j = i + 1 and repeat the process
'''