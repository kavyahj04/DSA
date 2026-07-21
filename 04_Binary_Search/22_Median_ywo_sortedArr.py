def medianOfSorted(a, b):
    l, r = 0, 0
    i2 = (len(a) + len(b)) // 2
    i1 = i2 - 1
    cnt = 0
    e1, e2 = -1,-1

    while(l<len(a) and r<len(b)):
        if(a[l]<= a[r]):
            if cnt == i1: e1 = a[l]
            if cnt == i2: e2 = a[l]
            l += 1
            cnt += 1
        else:
            if cnt == i1: e1 = b[r]
            if cnt == i2: e2 = b[r]
            r += 1
            cnt += 1
    while(l<len(a)-1):
        if cnt == i1: e1 = a[l]
        if cnt == i2: e2 = a[l]
        l += 1
        cnt += 1

    while(r<len(b)-1):
        if cnt == i1: e1 = b[r]
        if cnt == i2: e2 = b[r]
        r += 1
        cnt += 1
    
    if (len(a) + len(b)) % 2 == 0:
        print((e1 + e2) / 2)
        return (e1 + e2) / 2
    else:
        print(e2)
        return e2
    
a = [2]
b = [1]
medianOfSorted(a,b)