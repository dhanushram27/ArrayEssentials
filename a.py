def non_repeating_elements(arr):
    frequency = {}
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    non_repeating = [num for num, count in frequency.items() if count == 1]
    return non_repeating

arr = [ 2, 4, 5, 5, 3, 4, 7,8]
print(non_repeating_elements(arr))
