class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        #empty list to hold our values of x and y
        ans = []
        #Create our sublists that will be used to create ans
    
        i = 0
        j = len(nums) // 2
        while len(ans) < len(nums):
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1 
            j += 1
        return ans





#Problem
"""
Take a list and split it in half. The first half of the list becomes x, and the second half
becomes y after splitting the list in half create a new list by inputting the values of x and y
in alternating order.
"""
#Solution
"""
Create a new list ans that holds our newly ordered list. Create two pointers with one
at the beginning of the lift and one at the midpoint. Write a loop that 
appends the value of the first pointer to ans and the value of the second pointer 
Projected runtime O(n/2)
"""