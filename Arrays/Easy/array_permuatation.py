class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Define our new array that will hold the permutation
        ans = []
        """Write a loop that runs through our entire array sets 
        each value at i equal to nums[nums[i]] then append it to the
        end of our array ans. 
        """
        i = 0
        while i < len(nums):
            num = nums[nums[i]]
            ans.append(num)
            i += 1
        return ans 


array = [5,0,1,2,3,4]

attempt = Solution()

attempt.buildArray(array)
#Problem
"""
Arrange the values of the array nums in a different 
order without creating any values not in the original array 
"""
#Solution
"""
Create a loop that uses the values at the indexes of nums to
make a new list of those same values in a different order.
"""