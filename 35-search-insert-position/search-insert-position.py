class Solution(object):
    def searchInsert(self, nums, target):
        count = 0
        max_count = 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (nums[mid] == target):
                return mid
            
            elif (nums[mid] < target):
                left = mid + 1
            
            elif (nums[mid] > target):
                right = mid - 1

        return left
        