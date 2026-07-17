class FindTimesRotated:

    # anti clockwise rotation
    def findMin(self,nums):
        l, r = 0, len(nums) - 1
        ans, index  = nums[0], 0
        while l <= r:
            if nums[l] < nums[r]:
                index = l
                break
            mid = (l + r) // 2
            if nums[mid] < nums[index]:
                index = mid 
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        print(ans)
        return ans 
nums = [3,4,5,1,2]
find = FindTimesRotated()
find.findMin(nums)