# Bismillahir Rahmanir Rahim .
# Now i will make a programm that express today's nature.

# Variable taking from user.
t = float(input('How many celcius temerature today : '))

# Condition using.
if t <= 0:
	print('Today is the coldest day.')

elif t <= 17:
	print('Today is vary cold day.')

elif t <=25:
	print('It is tolerable day.')

elif t >=25:
	print('Today is vary hot day.')

else:
	print('Please write a valid number.')
