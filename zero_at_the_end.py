def zero_at_the_end(arr):
    n = len(arr)
    j = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j = j+1
    
    return arr

arrr = [2, 4, 4, 0, 0 ,4, 34, 22, 0]
print(zero_at_the_end(arrr))
