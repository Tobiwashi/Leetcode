class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        valid_employees = 0
        i = 0
        for hour in hours:
            if hours[i] >= target:
                valid_employees += 1
            i += 1

        return valid_employees



'''
Problem

Given an array of hours worked by employees return the amount of employees who worked up to or greater than the amount of target hours the employers set.
'''

'''
Solution

Create a variable named valid_employees that holds the value of the amount of employees that have worked the target hours. Simply iterate through the array of employees and write an if statement that checks if the hours worked is greater than or equal to the target hours if yes add 1 to the valid_employees variable and continue to increment the function. 
Worst Case O(n)
'''