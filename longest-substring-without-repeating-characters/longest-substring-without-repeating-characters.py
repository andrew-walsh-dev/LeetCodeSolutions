class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        max = 0
        for char in s:
            if char in substr:
                substr = substr.split(char)[1]
            substr += char
            if len(substr) > max:
                max = len(substr)
        return max
            