def diagonalDifference(arr):
    
    sum_a = 0
    sum_b = 0
    
    length = len(arr)
    
    print(length)
    for i in range(length):
        for j in range(length):
            if i == j:
                sum_a += arr[i][j]
            if i + j == length - 1:
                sum_b += arr[i][j]
    
    return(abs(sum_a - sum_b))
