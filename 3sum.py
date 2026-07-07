# BFA 

def sum3(nums):
    st = set()
    for i in range(len(nums)):
        temp = []
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 :
                    temp = [nums[i], nums[j], nums[k]]
                    st.add(tuple(sorted(temp)))
    print([list(t) for t in st])
    return [list(t) for t in st]

nums = [-1,0,1,2,-1,-4]
# sum3(nums)

# Time and Space complexity
# Time complexity: O(n³)
# Space complexity: O(n³) (worst case, for storing unique triplets in st) — auxiliary space excluding output is O(1) per iteration.


# Better Approach 

def sum3_2(nums):
    st = set()
    for i in range(len(nums)):
        hashSt = set()
        for j in range(i+1, len(nums)):
            third = -(nums[i] + nums[j])
            if third in hashSt:
                st.add(tuple(sorted([nums[i], nums[j],third])))
            hashSt.add(nums[j])
        
    print([list(t) for t in st])
    return [list(t) for t in st]

# sum3_2(nums)


# Optimal Approach 

def sum3_3(nums):
    ls = []
    for i in range(len(nums)):
        if i > 0  and num[i] != num[i-1]:
            continue
        j = i + 1
        k = len(arr) - 1
        while j < k:
            sum_ = nums[i] + nums[j] + nums[k]
            if sum_ > 0:
                k -= 1
            elif sum_ < 0:
                j += 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ls.append(temp)
                while j < k and nums[j] == nums[j -1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    print(ls)
    return ls

sum3_3(nums)
