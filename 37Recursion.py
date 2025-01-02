# Bismillahir Rahmanir Rahim
# Now I will learn about Recursion of Function.
# If a Function call himself it's called Recursion [ Punorabritty ].
# In this program we make a program that can solve Fectorial.
# Fectorial(x) = x*(x-1)*(x-2)*(x-3).....3*2*1

# Taking Input.
number = float(input("Which numer you want to do fectorial : "))

# Function of fectorial.
def fectorial(x):
	if x == 1:
		return 1
	else:
		return x*fectorial(x-1)

print(fectorial(number))

# In this program fectorial Function will call himself, so it's Recursion.
