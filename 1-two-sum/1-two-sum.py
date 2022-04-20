class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        dict = {}

        i = 0
        for num in nums:
            diff = target - num
            if diff in dict:
                return [i, dict[diff]]
            dict[num] = i
            i += 1