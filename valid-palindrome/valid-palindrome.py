

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = [char for char in s if char.isalnum()]
        alnumstr = ''.join(alnum).lower()
        return alnumstr == alnumstr[::-1]