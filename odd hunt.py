a,b = 7,7 

#Part 1: XOR Identity and equality
print("=== OddHunt ===")
print("a^a =", a^a )
print("a^0 =", a^0)
print("Equal (XOR):", (a^b) == 0)
print()

#Part 2: XOR cancellation 
arr = [3,5,3,5,9]
result = 0
for n in arr: result ^= n
print("XOR of" , arr, "=" , result)
print()

# Part 3: One occuring number
nums = [4,7,4,2,7,2,9]
res = 0
for n in nums: res ^= n 
print("Odd occuring:", res)
print()



# part 4: XOR of two Odd occuring numbers:-
pair = [3,9,3,5,5,7]
xab = 0
for n in pair: xab ^= n
print("XOR of two odds:" , xab,"->", bin(xab))
print()


#Part 5: split by rightmost set bit
setbit = xab & -xab
x,y = 0,0 
for n in pair:
    if n &setbit:x ^= n
    else: y^= n
print("Two odd occuring:",x, "and", y)