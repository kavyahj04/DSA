class FindPeakElement:
    def findElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                print(f"Found peak element at index {m} and num is {nums[m]}")
                return nums[m]
            elif nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m 
        print(f"Couldn't find peak element {l}")
        return -1

nums = [1,2,1,3,5,6,4]
element = FindPeakElement()
element.findElement(nums)