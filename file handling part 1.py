file_read = open('File handling.txt','r')
print("File in read mode:-")
print(file_read.read())
file_read.close()


file_write = open('File handling.txt','w')

file_write.write(" File in write mode:-")
file_write.write("Hi! I am vidit. I am 13 years old")
file_write.close()


file_append = open('File handling.txt','a')

file_append.write("\n File in append mode:-")
file_append.write("Hi! Iam vidit.Iam 13 years old.")
file_append.close()