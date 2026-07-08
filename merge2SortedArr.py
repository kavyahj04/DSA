# Optimal 1

def mergeArr(nums1, nums2, m, n):
    left = m - 1
    right = 0

    while left >= 0 and right < n:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    print(nums1, nums2)



# mergeArr(nums1, nums2, m, n)

# GAP Method 

def mergeArr2(nums1, nums2, m, n):
    l = m + n
    gap = (l // 2) + (l % 2)

    while gap > 0:
        left = 0
        right = left + gap
        while right < l:
            if left < m and right >= m:
                swapIfGreater(nums1, nums2, left, right - m)
            elif left >= m:
                swapIfGreater(nums2, nums2, left - m, right - m)
            else:
                swapIfGreater(nums1, nums1, left, right)
            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
    print(nums1, nums2)


def swapIfGreater(nums1, nums2, l, r):
    if nums1[l] > nums2[r]:
        nums1[l], nums2[r] = nums2[r], nums1[l]
    
nums1 = [1, 4, 7, 10] 
m = 4
nums2 = [2, 3, 5, 6]
n = 4
mergeArr2(nums1, nums2, m, n)

    

       
