# Program to count the number of lines in this files 
#opening the file
file = open("file 2.txt","r")
Counter = 0


# Reading from files
Content = file.read()
print(Content)
#splitting content into lines
#and storing them in a list 
CoList = Content.split("\n\n")
Counter=len(CoList)

print("This is the Number of lines which were in the file")
print(Counter)