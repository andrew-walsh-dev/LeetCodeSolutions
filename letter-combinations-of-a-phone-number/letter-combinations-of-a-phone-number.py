class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        arr = []
        def backtrack(i, current_str):
            if len(current_str) == len(digits):
                arr.append(current_str)
                return
            for c in map[digits[i]]:
                backtrack(i + 1, current_str + c)
        
        if digits == '':
            return []
        backtrack(0, '')
        return arr
        
            