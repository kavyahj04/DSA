def max1s(arr):
    counter = 0
    max_ = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            counter += 1
            if counter > max_:
                max_ = counter
        else:
            counter = 0
    print(max_)
    return max_

arr = [1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0]
max1s(arr)


# Single pass, two variables — O(n) time, O(1) space.