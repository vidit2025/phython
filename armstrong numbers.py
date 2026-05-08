# Take input from the user
number = int(input("Input your number: "))

#Calculate number of digits
digits = len(str(number))

#initialize result variable
resultNumber = 0

#find th esum of the a^digit
temp = number 
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digit 
    temp //=10
#display the result
if number == resultNumber:
    print(number,"is an Armstrong number")
else:
    print(number , "is not an Armstrong Number")