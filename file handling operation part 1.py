with open('project file.txt', 'w') as file:
    file.write("hi! I am penguin and i am 1 yr old.\n hello everyone.\n Welcome to codingal:3")


with open('project file.txt','r') as file:
    data = file.readlines()
    print(data)
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)