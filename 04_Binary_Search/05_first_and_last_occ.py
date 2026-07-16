# TO FIND FIRST AND LAST OCCURENCE - we have 3 solutions 


class FindOccurences:

    # BFA 
    def findOcc(self,nums, k):
        first, last = -1,-1
        for i in range(len(nums)):
            if nums[i] == k:
                if first == -1:
                    first = i
                last = i
        print(f"first - {first}")
        print(f"last - {last}")
        return [first, last]
    
    # T(n) - O(n)

    # Optimal 1
    def findOccBound(self,nums,k):
        first = self.low(nums, k)
        if first >= len(nums) or nums[first] != k:
            print(f"first - -1")
            print(f"last - -1")
            return [-1,-1]
        last = self.up(nums, k) - 1
        print(f"first - {first}")
        print(f"last - {last}")
        return [first, last]

    def low(self,nums, k):
        l,r = 0, len(nums) - 1
        first = len(nums)
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= k:
                first = m
                r = m - 1
            else:
                l = m + 1
        return first
    
    def up(self,nums, k):
        l,r = 0, len(nums) - 1
        last = len(nums)
        while l <= r:
            m = (l + r) // 2
            if nums[m] > k:
                last = m
                r = m - 1
            else:
                l = m + 1
        return last

    def findOccBinarySearch(self, nums, k):
        l, r = 0, len(nums) - 1
        first = self.findOccFirst(nums, k)
        last = self.findOccLast(nums, k)
        print(f"first - {first}")
        print(f"last - {last}")
        return [first, last]

    
    def findOccFirst(self, nums, k):
        l,r = 0, len(nums) - 1
        first = -1
        while l <= r :
            m = (l + r) // 2
            if nums[m] == k:
                first = m
                r = m - 1
            elif nums[m] < k:
                l = m + 1
            else:
                r = m - 1
        return first
    def findOccLast(self, nums, k):
        l,r = 0, len(nums) - 1
        last = -1
        while l <= r :
            m = (l + r) // 2
            if nums[m] == k:
                last = m
                l = m + 1
            elif nums[m] < k:
                l = m + 1
            else:
                r = m - 1
        return last
        

            
    


  
occ = FindOccurences()
nums = [5,7,7,8,8,10] 
target = 7
occ.findOcc(nums, target)
occ.findOccBound(nums, target)
elements = occ.findOccBinarySearch(nums, target)
if elements[0] != -1:
    print(f"Count of Occurences are - {elements[1] - elements[0] + 1}")
else:
    print(f"Count of Occurences are - 0")


