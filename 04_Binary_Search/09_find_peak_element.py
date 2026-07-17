class FindPeakElement:
    def findElement(self, nums):
        if len(nums) == 1:
            print(f"Found peak element at index {0} and num is {nums[0]}")
            return 0
        if nums[0] > nums[1]:
            print(f"Found peak element at index {0} and num is {nums[0]}")
            return nums[0]
        elif nums[len(nums) - 1] > nums[len(nums) - 2]:
            print(f"Found peak element at index {len(nums) - 1} and num is {nums[len(nums) - 1]}")
            return nums[len(nums) - 1]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                print(f"Found peak element at index {m} and num is {nums[m]}")
                return nums[m]
            elif nums[m] > nums[m-1]:
                l = m + 1
            else:
                r = m 
        print(f"Couldn't find peak element {l}")
        return -1

nums = [1,2,1,3,5,6,4]
element = FindPeakElement()
element.findElement(nums)

# T(n) - O(logn)