#fastest but doesn't maintain order
a = [2,2,5,8,7,6]
unique_elements = list(set(a))
print(unique_elements)

#Maintains Order
a = [2,2,5,8,7,6]
unique_elements = list(dict.fromkeys(a))
print(unique_elements)
