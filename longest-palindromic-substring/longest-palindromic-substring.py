class Solution:
    def longestPalindrome(self, str: str) -> str:
        max = str[0]
        for i in range(0, len(str)):
            for j in range(i, len(str)):
                substr = str[i : j + 1]
                if len(str) - i < len(max):
                    return max
                if substr == substr[::-1] and len(substr) > len(max):
                    max = substr
        return max