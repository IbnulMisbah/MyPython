# Bismillahir Rahmanir Rahim.
# Now i will learn Continue in Python . 
# Now i will determine summation of odd number in range 1 to 100 . 

sum = 0

for i in range (1 , 100):
    if i % 2 == 0:
        continue
    sum = sum + i

print("Summation of 1 to 100 odd number is",sum)