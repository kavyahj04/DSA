# union of an array

#bruteforce approach
def unionArray(arr1, arr2):
    print(list(set(arr1 + arr2)))
    return sorted(list(set(arr1 + arr2)))

arr1 = [1,1,2,3,4]
arr2 = [1,1,1,2,2,3,7,8]

# unionArray(arr1, arr2)

# Complexity:

# Time	O((n+m) log(n+m)) — dominated by sorted
# Space	O(n+m)


# optimal solution

def unionArraySortedOptimal(arr1, arr2):
    l, r = 0, 0
    m, n = len(arr1), len(arr2)
    temp = []
    def add(val):
        if not temp or temp[-1] != val:
            temp.append(val)

    while l < m and r < n:
        if arr1[l] < arr2[r]:
            add(arr1[l])
            l += 1
        elif arr1[l] > arr2[r]:
            add(arr2[r])
            r += 1
        else:
            add(arr1[l])
            l += 1
            r += 1
    while l < m:
        add(arr1[l]); l += 1
    while r < n:
        add(arr2[r]); r += 1
    print(temp)
    return temp

# unionArraySortedOptimal([1,1,2,2,3,4,5], [1,1,2,2,7,8])


#Complexity

# Time		O(n+m)
# Space		O(n+m)


# intersection of an array

def intersection(arr1, arr2):
    m, n = len(arr1), len(arr2)
    l, r = 0, 0
    temp = []
    def add(val):
        if not temp or temp[-1] != val:
            temp.append(val)
    while l < m and r < n:
        if arr1[l] == arr2[r]:
            add(arr1[l])
            l+=1
            r+=1
        elif arr1[l] < arr2[r]:
            l += 1
        else:
            r += 1
    
    print(temp)
    return temp

intersection([1,1,2,2,3,4,5], [1,1,2,2,7,8])

# complexity

# Time	O(m+n)
# Space	O(min(m,n)) — output only
