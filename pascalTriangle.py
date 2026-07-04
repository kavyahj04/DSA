# Given row and column, output the element
def pascalTriangle(row, col):
    res = 1
    for i in range(col):
        print(f"row {row}")
        print(f"col {col}")
        # print(f"{res}* ({row} - {i})")
        res = res * (row - i)
        # print(f"{res} // ({i} + 1)")
        res = res // (i + 1)
        
    print(f"element - {res}")
    return res

# # pass row -1, col -1
# row, col = 5, 1
# pascalTriangle(row-1, col-1)


# Print any given row

def pascal2(row):
    for i in range(row):
        print(pascalTriangle(row-1,i))

# pascal2(5)

def pascal2Optimal(row):
    ans = 1
    print(ans)
    for i in range(1,row):
        ans = ans * (row - i)
        ans = ans // i
        print(ans)
    # print(1)


pascal2Optimal(5)
