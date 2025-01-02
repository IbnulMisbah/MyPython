# Bismillahir Rahmanir Rahim. 
# Now i will make a program that can be determine Gosagu. 
# Gosagu = Greatest Common Divisor. 

a = float(input('Type bigger number : '))
b = float(input('Type small number  : '))

while b != 0:
    remainder = a % b
    a = b           # choto ta boro hobe
    b = remainder   # bakita hobe choto

print('Greatest Common Divisor is',a)  # gcd

# By Recursional way. 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(a, b))