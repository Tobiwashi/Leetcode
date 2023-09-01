class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        k = 0
        while i < len(nums):
            if nums[i] == nums[k]:
                i += 1
            else: 
                k += 1
                nums[k] = nums[i]
        return k + 1

''' 
Problem

Given an array nums that contains duplicates return the number of 
unique values in the array maintaining ascending order 

Intuition 

Given that it is an array question we'll most likely encounter the two pointer system
in order to avoid traversing the array back and forth

Solution

Create two pointers i and k and run a while loop that executes these operations
while i < nums length
checks to see if nums[i] = nums[k] that will mark a unique value so i will move but k will not
as k represents the number of unique values
if nums [i] =! nums[k] we will k++ to add to the number of unique values and set nums[i] = nums[k] until we've traversed
the entire list 
Time complexity O(n)
Space Complexity O(1)
'''