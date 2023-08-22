class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highest = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= highest:
                ans.append(True)
            else:
                ans.append(False)
        return ans








#Problem
"""
Find out if given all of the extra candies would a child at candies[i] would have the most amount of candy
(The value should not be stored after adding the extra candies.) 
Add the extra candy to the value of candies[i] and compare that with the values of the rest of the list.
"""