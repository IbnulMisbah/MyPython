# We know input() keep all data as a string variable .
# but we can change it & convart to integer,float or boolean variable .its called "Type Casting".
# we use to do this same function like int() , float() , str() & bool() .
# For example : int(input()) , float(input()) .

int = int(input("provide an integer number :"))
print ("Your number is",int,"& datatype is",type(int))

# python can't print any "floating number","string" & "boolean variable" in int() function .

float = float(input('Provide a real number :'))
print ("Your number is",float,"& datatype is",type(float))

# python can print int and float variables in float() function . but not str or bool .

str = str(input("write anything :"))
print ("You wrote",str,"& its type",type(str))

# str() function can print any variable .

bool = bool(input('Please input boolean variable :'))
print ("You wrote down",bool,'& its datatype',type(bool))

# Maybe bool() keep variable only first variable .
