class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #An array that will store our new summed values
        ans = []
        sum = 0 
        i = 0
        for num in nums:
           sum = nums[i] + sum
           ans.append(sum)
           i += 1
        return ans







#Problem
"""
For every index in an array return the add the sum of the previous indexes to the next index ex. if nums = [1,5,10,15]
the expected return would be [1, 6, 16, 31]
"""

#Solution
"""
create an array ans to store the values of our running sums function. Set a variable sum = 0 and write a for loop that makes sum = sum + nums[i] and append the sum to a new array.
"""