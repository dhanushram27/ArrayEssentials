a = [10,56,34,82,23,43]
max_element = a[0]
min_element = a[0]

for i in range (len(a)):
    if max_element < a[i]:
        max_element = a[i]
    
    if min_element > a[i]:
        min_element = a[i]
        
print("Largest Elementin the Array :", max_element)
print("Smallest Element in the Array :", min_element)
