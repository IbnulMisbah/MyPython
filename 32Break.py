# Bismillahir Rahmanir Rahim .
# Now i will learn about Break on Python. 

# Simple a List or an Array.
fruits = ['apple','mango','kathal','lichi',"jam","jambura",'Jamrul']

# Now I will search jam. 
found = 'no'
for fruit in fruits:
    if fruit == 'jam':
        found = 'yes'
        break
if found == 'yes':
    print('Yes, I have Jam.')
else:
    print("Sorry,I don't have.")

# Now I will search jam in onother way. 
if 'jam' in fruits:
    print ("Yes, I have jam.")
if 'jam' not in fruits :
    print("Sorry, I don't have jam.")

# More another way. 
if 'jam' in fruits:
    print('Yes, I have jam.')
else:print("Sorry")