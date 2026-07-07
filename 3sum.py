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
sum3(nums)