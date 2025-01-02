# Now,I will learn Comperasion Operator.
# Comperasion Operators : (>),(>=),(<),(<=) .
# greater than >,greater than or equal >=,less than <,less than or equal <=.

# Simple variable . Here "m" means Money .
m = float(input("How many money you have : "))

# Using Codition with Comperasion Operator.
if m < 1:
	print("OH NO.You have no money.")

elif m <= 5:
	print("You can eat chocollat.")

elif m <= 10:
	print('You can eat chocollat or lollypop or cheaps.')

elif m <= 20:
	print('You can eat chocollat or lollypop or cheaps or joose.')

elif m <=50:
	print('You can eat chocollat or lollypop or cheaps or joose or cold drinks.')

elif m <= 100:
	print('You can eat chocollat or lollypop or cheaps or joose or cold drinks.')
	print('Or you can buy a small book.')

elif m <= 200:
	print('You can eat many things or buy a small book.')

elif m <= 400:
	print('You can buy many books.')

elif m <= 1000:
	print('You can eat many things and buy many book.')

elif m <= 5000:
	print('You can buy many books or any featcher phone.')

elif m <= 15000:
	print('You can buy many books or RaspberryPi or a smart phone.')

elif m > 15000:
	print('You can buy many books or a cycle or a computer.')

else:print('Made by Hizbullah.')
