a = [10, 89, 9, 56, 4, 80, 8]
min_element = a[0]

for i in range (len(a)):
    if min_element > a[i]:
        min_element = a[i]

print(min_element)
