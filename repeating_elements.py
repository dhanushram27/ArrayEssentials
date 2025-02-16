def repeating_elements(arr):
    frequency = {}
    repeating_element = []
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    for key,value in frequency.items():
        if value > 1:
            repeating_element.append(key)
    
    return repeating_element

arr2 = input("Enter The array : ")
arr1 = list(map(int, arr2.split()))
print(repeating_elements(arr1))
