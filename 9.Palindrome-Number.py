'''
# class Solution:

def iterate_digits(number):
    
    number_str = str(number)

    for digit in number_str:

        print(digit)

iterate_digits(123456789)'''

'''
# class Solution:

def isPalindrome(number):

    number_str = str(number)

    return number_str == number_str[::-1]

print(isPalindrome(12321))
print(isPalindrome(12345))'''
class Solution:
    def isPalindrome(self, number):
        # We added self as the first parameter in the isPalindrome method within the Solution class, as required for instance methods in Python classes

        # Convert the given number to a string
        number_str = str(number)
    
        # Determine the length of the number
        length = len(number_str)
    
        # Iterate through the first half of the digits to compare with the corresponding digits from the end
        for i in range(length // 2):
        
            # Check whether the digit at index i from the beginning matches the digit at index length - i - 1 from the end
            # If the two digits don't match, the number is not a palindrome, so return False immediately
            if number_str[i] != number_str[length - i - 1]: 
                return False

        # If all corresponding digits match, the number is a palindrome, so return True
        return True

solution = Solution()
print(solution.isPalindrome(12321))         # Output: True
print(solution.isPalindrome(12345))         # Output: False
print(solution.isPalindrome(12345654321))   # Output: True
print(solution.isPalindrome(12345654322))   # Output: False



