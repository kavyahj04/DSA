class FindMinimum:
    def findElem(nums):
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            print(f"Minimum element is {res}")
            return res
nums = [4,5,6,7,0,1,2]
findMin = FindMinimum()
findMin.findElem(nums)
