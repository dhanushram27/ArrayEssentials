def find_smallest_element(arr):
    if len(arr) < 2:
        return "Array Need To Have Two Element"
    
    first = second = float('inf')
    
    for num in arr:
        if num < first:
            second = first
            first = num
            
        elif num < second and num != first:
            second = num
    
    return second
    
arr = [23, 45, 77, 12, 34, 67, 21]
print("Second Largest Element is :", find_smallest_element(arr))
