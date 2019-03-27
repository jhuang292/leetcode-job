class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        if len(nums) == 0:
            return [-1,-1]
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            result.append(start)
        elif nums[end] == target:
            result.append(end)
        else:
            result.append(-1)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            result.append(end)
        elif nums[start] == target:
            result.append(start)
        else:
            result.append(-1)
        
        return result
