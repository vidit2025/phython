lst= ['apple','Guava','mango','banana','kiwi']

print("Length of list:",len(lst))
print("First element:", lst[0])
print("Last element",lst[-1])

lst.append('papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()#assending order
print("sorted list :", lst)

lst.sort(reverse=True)#Dessending order
print("Sorted list:", lst)

lst.pop(1)
print("Updated list :", lst)

lst.reverse()
print("Reversed List :", lst*2)

lst= lst[:5]
print("Sliced List:", lst)

lst.clear()
print("Updated list:", lst)