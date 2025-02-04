def sum_of_elements(arr):
    sum = 0
    
    for i in range (len(arr)):
        sum = sum + arr[i]
    return sum
        
arr = [10, 89, 9, 56, 4, 80, 8]
print("Sum of an Array :", sum_of_elements(arr))
