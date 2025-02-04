a = [0,34, 56,32,788,33,7949,5]
max_element = a[0]

for i  in range (len(a)):
    if max_element < a[i]:
        max_element = a[i]

print(max_element)
