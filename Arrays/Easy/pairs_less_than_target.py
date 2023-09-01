class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pairs = 0
        sorted_nums = nums.sort()
        l_pointer = 0
        r_pointer = len(nums) - 1
        while (l_pointer < r_pointer):
            if (nums[l_pointer] + nums[r_pointer] < target):
                pairs += r_pointer - l_pointer
                l_pointer += 1
            else:
                r_pointer -= 1
        return pairs
    
'''
Problem: You're given an array of integers and a target value. The task is to count the number of pairs of elements in the array such that the sum of the pair is less than the target value.
The key insight for solving this problem is recognizing that if you have an array sorted in ascending order, you can efficiently find pairs that meet the given condition using a Two-Pointers Approach.


The Two-Pointers Approach is a common technique to solve problems involving arrays or sequences. In this case, you can use two pointers, often referred to as the "left" and "right" pointers, to traverse the array and find pairs that satisfy the given condition.

Here's a high-level overview of the approach:

1.) Sort the array in ascending order. Sorting helps in efficiently exploring pairs with sums less than the target value.

2.) Initialize two pointers, left and right, pointing to the first and last elements of the sorted array, respectively.

3.) Initialize a variable count to keep track of the count of valid pairs.
While the left pointer is less than the right pointer:
If the sum of the elements at left and right is less than the target value, it means all pairs with the current left element will also satisfy the condition. So, increment the count by right - left and move the left pointer to the right.
If the sum is greater than or equal to the target, move the right pointer to the left.

4.) Continue this process until the left pointer crosses the right pointer.

Time complexity: O(nlogn)
Sorting the array takes O(n log n) time, where n is the number of elements in the array. The two-pointer traversal takes linear time, O(n), as each element is visited once.
Overall, the time complexity is dominated by the sorting step, making it O(n log n).

Space complexity: O(1)
The space complexity depends on the sorting algorithm used. If you're using an in-place sorting algorithm like Quicksort, the space complexity will be O(1) (negligible). If you're using an algorithm that requires additional space, the space complexity might be higher.
'''