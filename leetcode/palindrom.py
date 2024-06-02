# https://www.youtube.com/watch?v=OlTk8wM48ww&ab_channel=AlgoEngine

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
