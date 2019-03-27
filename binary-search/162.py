class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[end] > nums[start]:
            return end
        else:
            return start
