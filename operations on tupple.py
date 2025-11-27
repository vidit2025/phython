#empty tupple
my_tuple =()
print(my_tuple)

#tupple having integers
my_tuple =(1,2,3)
print(my_tuple)

#tuple with mixed datatypes
my_tuple=(1,"hello",3.4,1)
print(my_tuple)

#Nested tuple
my_tuple =("mouse", [8,4,6], (1,2,3))
print(my_tuple)

# accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])

#nested tuple
n_tuple =("mouse",[8,4,6],(1,2,3))

#nested index 
print(n_tuple[0][3])

# Slicing
print("sliced :",my_tuple[1:4])

# Iterating through tuple
for letter in n_tuple:
    print("Hello", letter)