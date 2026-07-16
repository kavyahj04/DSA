class SeachElement:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def searchInSorted(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                print(f"The search Index position is - {m}")
                return m
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        print(f"The search Index position is - {m}")
        return m

nums = [4,5,6,7,0,1,2]
target = 6
search = SeachElement(nums, target)
search.searchInSorted(search.nums, search.target)

# T(n) - O(n)


