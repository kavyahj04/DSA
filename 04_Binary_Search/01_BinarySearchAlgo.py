class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        return self.binarySearch(nums,low, high, target)
        
    def binarySearch(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        return self.binarySearch(nums, low, mid-1, target)
        