# Bismillahir Rahmanir Rahim. 
# Now i will make a program that prints Even and Odd numbers. 

start = int(input("Write down your first Odd number : "))
stop  = int(input("Write down your last Odd number  : "))

stat2 = int(input("Write down your first Even number : "))
stop2 = int(input("Write down your last Even number  : "))

# Printing Odd number Using For loop .
for i in range (start , stop+1 , 2):
    print(i)

print(15*"#")

# Printing Odd number Using while loop . 
i=start 
while i < stop+1 :
    print(i)
    i = i+2

print(30*"*")

# Printing Even number by for loop . 
for i in range (stat2 , stop2+1 , 2):
    print(i)

print(15*"#")

# Printing Even number by while loop . 
i = stat2
while i < stop2+1:
    print(i)
    i = i+2

print(30*'#')

# This program is incompleted. 