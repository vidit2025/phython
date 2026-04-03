
#Read first line of the file
file  = open('file 2.txt','r')
print("Reading first line....")
print(file.readline())
file.close()


#Read first three lines 
file = open('file 2.txt','r')
print("Reading the first three lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#loping here through all the lines of the files  and we are using here two other ways but itresults the same 
file = open('file 2.txt','r')
print("Looping through all lines...")
for line in file:
    print(line)
file.close()

# second way
file =open('file 2.txt','r')
print( "reading all lines in the form of list...")
for f in file.readlines():
    print(f)

#Read first line of the file
file  = open('file 2.txt','r')
print("Reading first line....")
print(file.readline())
file.close()


#Read first three lines 
file = open('file 2.txt','r')
print("Reading the first three lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#loping here through all the lines of the files  and we are using here two other ways but itresults the same 
file = open('file 2.txt','r')
print("Looping through all lines...")
for line in file:
    print(line)
file.close()

# second way
file =open('file 2.txt','r')
print( "reading all lines in the form of list...")
for f in file.readlines():
    print(f)
file.close()    