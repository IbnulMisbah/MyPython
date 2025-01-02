# Bismillahir Rahmanir Rahim.
# Now i will learn real use of Boolean Operator & Comperasion Operator.
# Now i will make a program that determines our Nilkhet Visiting.
# Python use forword-slash [/] for Division & back-slash for code-breaks.
# [\n] used for breaking line.

# Input taking from us.
day = input('What day is today ? ')
mn1 = float(input('How many money Hukush has ? '))
mn2 = float(input('How many money Pakuhs has ? '))
money = mn1+mn2

# Using Condition .Boolean & Compearsion Operator.
if day=='sunday' or day=='monday' or day=='tuesday' or day=='wensday'\
                    or day=='wednesday' or day=='thursday':
	print('OH NO,Today you have to go to Madrasah.\nYou can not go to Nilkhet.')

elif (day=='friday' or day=='saturday') and ( money >= 500 or ( mn1 >= 500 or mn2 >=500 )):
	print("Hukush-Pakush can buy many books and eat many things.")

elif (day=='friday' or day=='saturday') and ( money >= 300 or ( mn1 >= 300 or mn2 >= 300)):
	print("Hukush-Pakush can go to Nilkhet and buy some books.")

elif (day=='friday' or day=='saturday') and ( money >=160 or (mn1 >=160 or mn2>=160)):
    print("Hukush-Pakush can go to Nilkhet and come back from Nilkhet but can't buy any book")

elif (day=='friday' or day=='saturday') and money < 160:
   print("Hukush-Pakush can't go to Nilkhet.")

else:print("Please,Write down valid inputs.")
