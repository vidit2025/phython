#Power surge 
#Topics:n&(n-1) trick | Power of 2 | Power of 4| Power of 8| Binary Exponentiation

n = 12  #binary:1100

#Part 1: The n & (n-1) trick
print("===Power Surge ===")
print("n        =",n, "->", bin(n))
print("n - 1  =", n - 1, "->", bin(n-1))
print("n&(n-1) =", n & (n-1), "->" , bin(n &(n - 1)))
print()

# Part 2: Power of 2 check ":
print("Power of 2 check :")
for x in [1,4,6,16,18,64]:
    result = x> 0  and (x & (x -1)) == 0     # True if only one bit is set
    print(" ", x, "->", bin(x),  "->", result)
print()

# Part 3 :Power of 4 check 
def pow4(n): 
    if n <= 0 or n & (n - 1) != 0:  # must be a power of 2 first
        return False
    count = 0
    while n > 1:
        n = n >> 1 # right-shift: move one bit to the right
        count = count + 1
    return count % 2 == 0  #power of 4 means a bit is at an even position

print("Power of 4 check:")
for x in [1,4,8,7,5,3,16,32,64]:
    print(" ", x, "->", pow4(x))
print()

