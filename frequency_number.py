def frequency_number(arr):
    freq = {}
    
    for element in arr:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq
    
arr = [5,6,6,7,3,5,6,2,1]
print(frequency_number(arr))
