class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i

'''
Problem

Find the indicies of the two Numbers that add up to target and return them in an array
'''

'''
Create a hasmap in which the key stores the value of the index and check to see if the difference between that value is in our array if so return that value and the current value of i in an array
'''