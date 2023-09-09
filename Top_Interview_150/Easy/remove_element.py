class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i





'''
Problem
Given a value remove all values in nums matching val as an int k from the array and return the amount of elements not = to k. However, the first k amount of values should contain every value not = to k. All changes must be made inline meaning it has to have a space complexity of O(1)
'''

'''
Solution

Time Complexity: O(n)
Space Complexity: O(1)

Could Not Solve
Found Solution from Neetcode https://youtu.be/pGKDzt0gk-A
'''