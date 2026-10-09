class Solution(object):
    def singleNumber(self, nums):
        unique = 0

        for i in range(len(nums)):
            
                unique = unique ^ nums[i]
        return unique        