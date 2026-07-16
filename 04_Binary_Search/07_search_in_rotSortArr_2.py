class SeachElement:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def searchInSorted(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                print("Num Found")
                return True
            if nums[l] == nums[m] and nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
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
        print("Num not Found")
        return -1

nums = [1, 0, 1, 1, 1]
target = 1
search = SeachElement(nums, target)
search.searchInSorted(search.nums, search.target)

# T(n) = O(logn)
# if lot of duplicates - we can shrink all elements -  O(n/2)
