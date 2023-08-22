class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        #An Array that will hold all the max wealths of our array and will then return the largest one
        ans = []
        for account in accounts:
            ans.append(sum(account))
        
        return max(ans)







#Problem
"""
Given a list of arrays containing peoples wealth return the greatest wealth of any one account
"""

#Solution
"""
Write a loop that adds the values of each accounts wealth using the sum() function adding it to an array and calling the max() function on
that array that will return the highest wealth
"""