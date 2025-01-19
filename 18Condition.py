# Now , i will learn Condition in python .
# Three Condition will be learned by me : if , elif (else if) , else .
# Here if & elif is condition , else is solution .
# In this program i will use Boolean operator : Equal-Equal(==) operator.
# In condition's statement ,we have to follow indentation (Tab or 4 spaces).

# 1st we take a variable with condition from user .
# v means Value.
v = int(input("Write down a single number (1-5) : "))

# now we write if condition and its statement with indentation.
if v == 1:
	print("You wrote One")

# now we write elif condition.
# if the above condition dosen't fullfilled , Programm will come in this condition.
elif v == 2:
	print("You wrote Two")

elif v == 3:
    print("You wrote Three")

elif v == 4:
    print("You wrote Four")

elif v == 5:
    print("You wrote Five")

# if the above any condition dosen't fullfilled , Programm will not do anything .
# But now we use soluion (else).

else:
    print("You didn't follow condition")
