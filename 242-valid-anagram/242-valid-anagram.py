class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        s_chars = {}
        t_chars = {}
        
        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1
        
        for char in s_chars:
            if s_chars.get(char) != t_chars.get(char):
                return False
            
        return True