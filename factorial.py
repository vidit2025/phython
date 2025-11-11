def recur_factorial(n) :
     if n==1:
           return 1 
     else:
           return n*recur_factorial(n-1)
     
n=int(input("Enter a number"))
if (n<0):
    print("Factorial doesn't exist for negative numbers.")
elif(n==0):
     print("Factorial of 0 is 1.")
else:
     print(f"Factorial of {n} is {recur_factorial(n)}")         
     
     