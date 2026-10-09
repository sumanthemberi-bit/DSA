class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        

        n = len(nums)
        dum = [0] * n
        k = k % n
        
        for i in range(n-k,n):
            dum[i - (n - k)] = nums[i]
        for i in range(n-k): 
            dum[k + i] = nums[i] 
        
        for i in range(n):
            nums[i] = dum[i]
        