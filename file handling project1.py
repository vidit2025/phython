file = open( 'project file.txt','r')
print(file.read())
file.close()


file = open('file 2.txt' ,'r' )
print("\n Read in parts \n")
print(file.read(12))
file.close()

file = open('project file.txt', 'r')
print("Now reading the first line in the file")
print(file.readline())
file.close()

file = open('project file.txt','r')
print("Now here I am going to read to read three lines of the file...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('project file.txt','r')
print("reading all the from the file and making a list")
for f in file.readlines():
    print(f)
file.close()

file = open('project file.txt' ,'a')
file.write("Hi! I am a student and my name is vidit and istudy in codingal.")
file.close()