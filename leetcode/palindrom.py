# https://www.youtube.com/watch?v=OlTk8wM48ww&ab_channel=AlgoEngine
# The idea here is that we don't need to reverse all the digits, only half the digits.
# The first line checks some edge cases, and returns False immediately if the number is negative or ends with a 0
# (with the exception of the number 0 itself). The loop then uses the modulo and floor division operators to reverse the digits and transfer them to the half variable.

# Once the halfway point is reached, we return True if the two halves are equal to each other.
# If the number originally had an odd number of digits, then the two halves will be off by 1 digit, so we also remove that digit using floor division, then compare for equality.

class Solution:
    def isPalindrome(self, x: int) -> bool:  # Check if the integer is a palindrome
        if x < 0 or (x != 0 and x % 10 == 0):  # If negative or ending with 0 (except for 0 itself), it's not a palindrome
            return False

        half = 0  # Initialize variable to store the first half of the reversed number
        while x > half:  # Iterate until the first half is greater than the remaining part of the number
            half = (half * 10) + (x % 10)  # Build the reversed first half of the number
            x = x // 10  # Move to the next digit by integer division

        return x == half or x == half // 10  # Check if it's a palindrome considering both odd and even length

    def isPalindromeString(self, s: str) -> bool:  # Check if the string is a palindrome
        x = str(s)  # Convert the input string to a string (not necessary but for consistency)
        return x == x[::-1]  # Check if the string is equal to its reverse


isPalindrome = Solution().isPalindrome
print(isPalindrome(123))
print(isPalindrome(121))

isPalindrome = Solution().isPalindromeString
print(isPalindrome("abc"))
print(isPalindrome("abab"))
print(isPalindrome(121))

