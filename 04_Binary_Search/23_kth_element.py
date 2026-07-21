def medianOfSorted(a, b, k):
    l, r = 0, 0
    cnt = 0

    while(l<len(a) and r<len(b)):
        if(a[l]<= b[r]):
            if cnt == k: return a[l]
            if cnt == k: return a[l]
            l += 1
            cnt += 1
        else:
            if cnt == k: return b[r]
            if cnt == k: return b[r]
            r += 1
            cnt += 1
    while(l<len(a)):
        if cnt == k: return a[l]
        if cnt == k: return a[l]
        l += 1
        cnt += 1

    while(r<len(b)):
        if cnt == k: return b[r]
        if cnt == k: return b[r]
        r += 1
        cnt += 1
    
    
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
medianOfSorted(a,b,k)