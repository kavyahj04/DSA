
# Brute Force
def sum4(nums, target):
    st = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j + 1, len(nums)):
                for l in range(k +1, len(nums)):
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l] 
                    if sum_ == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        st.add(tuple(sorted(temp)))
    print([list(t) for t in st])
    return [list(t) for t in st]

nums = [1,0,-1,0,-2,2]
target = 0
# sum4(nums, target)


# Better 

def sum4_2(nums, target):
    
    st = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            hashst = set()
            for k in range(j+1,len(nums)):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in hashst:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    st.add(tuple(sorted(temp)))
                hashst.add(nums[k])
    print([list(t) for t in st])
    return [list(t) for t in st]

# sum4_2(nums, target)

# Optimal 

def sum4_3(nums, target):
    st = set()
    nums = sorted(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i+1, len(nums)):
            if j > i + 1 and nums[j] == nums[j -1]:
                continue
            k = j + 1
            l = len(nums) - 1
            while k < l:
                sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                if sum_ > target:
                    l -= 1
                elif sum_ < target:
                    k += 1
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    st.add(tuple(sorted(temp)))
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    print([list(t) for t in st])
    return [list(t) for t in st]

sum4_3(nums, target)