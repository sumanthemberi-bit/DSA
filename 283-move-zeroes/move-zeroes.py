class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        zero = [0] * n 
        
        for i in range(n):
            if (nums[i] != 0):
                zero[count] = nums[i]
                count += 1
        
        # for i in range(n):
        #     if (nums[i] != 0):
        #         zero[count] = nums[i]
        
        # for i in range(n - count,n):
        #     zero[i] = 0

        for i in range(n):
            nums[i] = zero[i]
        