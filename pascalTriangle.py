# Given row and column, output the element
def pascalTriangle(row, col):
    res = 1
    for i in range(col):
        print(f"row {row}")
        print(f"col {col}")
        print(f"{res}* ({row} - {i})")
        res = res * (row - i)
        print(f"{res} // ({i} + 1)")
        res = res // (i + 1)
        
    print(res)
    return res

# pass row -1, col -1
row, col = 5, 1
pascalTriangle(row-1, col-1)