file = open( 'file 2.txt','r')
print(file.read())
file.close()


file = open('file 2.txt' ,'r' )
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('file 2.txt' ,'a')
file.write("Hi iam vidit and I am 13 years old.")
file.close()