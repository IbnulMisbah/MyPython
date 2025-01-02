# Bismillahir Rahmanir Rahim.
# Now I will make a calculator by Python.
# In this programm i will use print(),input(),float(),if,elif,else etc.

# Announcement.
print('####################################################################################################')
print('####################################################################################################')
print('                                    Bismillahir Rahmanir Rahim.                                     ')
print('                 It is a simple Calculator.You can use it for simple mathematics.                   ')
print('       Firstly you have to input 1st number ,Arithmatic operators (+-*/^%) & then 2nd number.       ')
print("   Arithmatic Operators : Plus(+),Minus(-),Multiply(*),Divide(/),Power(^) & Modulo(%).So let's go.  ")

# Variable Taking.f=First number,o=Operators,s=Second number.

f =  float(input('                                Write Down your first number : '))
o =  input('                                  Input an Operator [+-*/^%] : ')
s =  float(input('                               Write down your second number : '))

# Codition using.

if o == '+':
	res = f+s

elif o == '-':
	res = f-s

elif o == '*':
	res = f*s

elif o == '/':
	res = f/s

elif o == '%':
	res = f%s

elif o == '^':
	res = f**s

else:
	print("                      You entered a wrong operator.The program will crash now.")

print("                                     ",f,o,s,"=",res)
print("                                This program developed by Hizbullah.")
print('####################################################################################################')
print('####################################################################################################')
