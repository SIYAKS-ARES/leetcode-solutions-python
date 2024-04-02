'''This line defines a class named Solution that inherits from object.
In Python 2, explicitly inheriting from object creates a new-style class.
In Python 3, all classes are new-style classes by default.'''
class Solution(object):
    def twoSum(self, nums, target):
        # "self" is a reference to the instance of the class. It's used to access other methods or variables within the class.
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            '''For each num in the nums list, this line calculates the complement,
            which is the difference between the target and the current num.
            This is the number that, when added to num, will result in the target sum.'''
            if complement in num_indices:
                '''This line checks if the complement is already present in the num_indices dictionary.
                If it is, it means we've found a pair of numbers that sum up to the target.'''
                return [num_indices[complement], i]
                '''If the complement is found in num_indices,
                this line returns a list containing the indices of the two numbers that sum up to the target.
                The first index is the index of the complement, and the second index is the current index i.'''
            num_indices[num] = i
        return None
        '''If no such pair is found after iterating through the entire nums list,
        this line returns None to indicate that there is no solution.'''

solution = Solution()
# Finally, this code creates an instance of the Solution class named solution.
nums = [2, 7, 4, 3, 6]
target = 9
print(solution.twoSum(nums, target)) # Output: [0, 1]
'''It calls the twoSum method of the solution instance with nums and target as arguments.
It prints the result of the method call,
which will either be the indices of the two numbers that sum up to the target or None if no such pair exists.'''