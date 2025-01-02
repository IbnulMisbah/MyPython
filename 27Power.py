# Bismillahir Rahmanir Rahim.
# Now i will make Power box.
# The program will take Base and Power from user and give value.

# Taking input.
base = float(input("Please write down Base : "))
power= float(input("Please write down Power : "))
bs1 = base
i = 1

if power > 0:
	while i < power:
		i = i+1
		base = base*bs1
	print(bs1,"to the power",power,"=",base)

elif power < 0:
	i=-1
	while i > power:
		i = i-1
		base = base*bs1
	print(bs1,"to the power",power,"= ( 1 /",base,")")

elif power == 0:
	print(bs1,"to the power",power,"= 1.0")
