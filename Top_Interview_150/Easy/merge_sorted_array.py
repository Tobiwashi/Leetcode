class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = m
        right = 0

        for num in nums2:
            nums1[left] = nums2[right]
            right += 1
            left += 1
        return nums1.sort()
 


'''
Problem

Merge two arrays nums1 and nums2 that are sorted in ascending order by inserting nums1 into nums2 while still having them
sorted in ascending order. The lists must be merged in line and cannot be combined with the use of any extra memory and must be modified in line.
'''

'''
Solution

Time Complexity: O(n)
Space Complexity: O(1)
Create two pointers "left" and "right" initialize left at nums[m] which is the first empty space in the array.
Create a for loop that sets the value of nums1[left] to nums2[right] and increment both pointers since we know that 
the length of the array will always have just enough room to accomodate n. Then set nums1 = nums1.sort() and return that nums1
'''