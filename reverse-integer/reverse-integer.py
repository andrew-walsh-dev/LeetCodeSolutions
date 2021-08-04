class Solution:
    def reverse(self, x: int) -> int:
        if ('-' in str(x)):
            rev = int(str(x * -1)[::-1]) * -1
        else:
            rev = int(str(x)[::-1])
        
        if rev not in range(-2**31, 2**31 - 1):
            return 0
        return rev