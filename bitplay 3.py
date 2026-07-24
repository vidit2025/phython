#BITPLAY 3
#TOPICS : arithmetic swap | XOR swap |left shift | divide without /

a = 56
b = 12

#part 1 swap using addition and substraction
print("=== Bitplay 3 ===")
print("Before:a =", a, " b=", b)
a = a + b
b = a - b
a = a - b
print(" Swapped: a=",a,"b =",b)
print()

# PART 2 : Swap using XOR
a = 56
b = 12
a = a ^ b
b = a ^ b
a = a ^ b
print("XOR swap: a =", a,  " b =", b)
print()

#Part 3 left shift doubles the number each time 
print("Left shift:")
print(" 3<<1 =", 3<<1)
print(" 3<<2 =", 3<<2)
print(" 3<<3 =", 3<<3)
print("3<<4 =", 3<<4)
print(" 3<<5 =",  3<<5)
print()

