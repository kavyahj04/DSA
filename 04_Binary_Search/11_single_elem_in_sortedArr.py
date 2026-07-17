class SingleElement:
    def singleNonDuplicate(self, nums):
        n = len(nums) - 1
        if nums[0] != nums[1]:
            print(f"Single Elemenet is {nums[l]}")
            return nums[l]
        elif nums[n] != nums[n - 1]:
            print(f"Single Elemenet is {nums[n]}")
            return nums[n]
        l, r = 1, n - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                print(f"Single Elemenet is {nums[m]}")
                return nums[m]
            if ((m % 2 != 0) and nums[m] == nums[m - 1]) or ((m % 2 == 0) and nums[m] == nums[m + 1]):
                l = m + 1
            else:
                r = m - 1

nums = [3,3,7,7,10,11,11]
single = SingleElement()
single.singleNonDuplicate(nums)