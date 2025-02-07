arr = [15, 12, 19, 11, 16, 13, 18, 17, 14, 10]
arr.sort()
mid = len(arr)//2
first = arr[:mid]
second = arr[mid:][::-1]
print(first + second)
