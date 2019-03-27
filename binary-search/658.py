class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.find_upper_closest_element(arr, x)
        left = right - 1
        
        results = []
        for _ in range(k):
            if self.is_left_closer(arr, left, right, x):
                results.append(arr[left])
                left -= 1
            else:
                results.append(arr[right])
                right += 1
        return sorted(results)
        
        
    def find_upper_closest_element(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
                
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end + 1
    
    def is_left_closer(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
