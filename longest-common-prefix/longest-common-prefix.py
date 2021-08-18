class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        prefix = ''
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for str in strs:
                if curr != str[i]:
                    return prefix
            prefix += curr
        return prefix