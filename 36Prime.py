# Bismillahir Rahmanir Rahim . 
# Now i will make a program that understands Prime number. 
# I will make it by function .

for x in range(2, 100):
    is_prime = True

    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print(x)
