# Bismillahir Rahmanir Rahim.
# Now i will make a power box by for loop.

# Taking Input.
bases = float(input("Write down your Bases : "))
power = int(input('Write down your Power : '))
base  = bases

# Using for loop under if Condition
if power > 0:
	for i in range (power-1):
		bases = bases*base
	print(base,'to the power',power,"=",bases)

elif power < 0:
	i = -1
	while i > power:
		bases = bases*base
		i = i-1
	print(base,'to the power',power,"= ( 1 /",bases,')')

else :
	bases = 1
	print(base,'to the power',power,"=",bases)
