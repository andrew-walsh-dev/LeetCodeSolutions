class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        _s = s.split(' ')
        return len(_s[len(_s) - 1])