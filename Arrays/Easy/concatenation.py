class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Array to store the values of our new concatenation
        ans = []
        #Loop that appends the values of nums a nums^2 amount of times
        i = 0
        while len(ans) < len(nums) * 2:
            if i == len(nums):
                i = 0
            else:
                ans.append(nums[i])
                i += 1
        return ans

attempt = Solution()
array = [1,2,1]
print(attempt.getConcatenation(array))




#Problem
"""
Create an array that returns the concatenation of a given array "nums"
i.e. nums * 2, or all values in the array twice example nums = [1,2,3]
ans = [1,2,3,1,2,3]
"""

#Solution
"""
Create an empty array ans to hold our new concatenation of nums.
Make a loop that runs while len(ans) < len(nums) * 2. appending the value of nums[i]
to the end of ans set i = 0 when i = len(nums) in order to repeat all the values of n
projected runtime of O(n^2)
"""