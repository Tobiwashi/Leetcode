class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        #Our initial variable that will have the operations performed on it.
        X = 0
        #Iterator
        i = 0
        #A while loop that traverses our array and checks if the given value of i is X++ or X--
        while i < len(operations):
            if operations[i] == "X++":
                X += 1 
            if operations[i] == "++X": 
                X += 1
            if operations[i] == "X--":             
                X -= 1 
            if operations[i] == "--X":
                X -= 1
            i += 1
        return X





#Problem
"""
Turn a given set of strings into different operations of mathematics, perform those operations,
and return the result of the completion of those operations
"""

#Solution
"""
Create a loop with an if statement that performs the desired operation based on the content of the string
by checking the contents of the string against the given operation parameters. Return the result as an int
Projected O(n) time.
"""