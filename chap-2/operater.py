# Arthimatic operators -> +,-,*,/
a = 1
b =  2
c = a + b
print(c)

# Assignment operators -> =,+=,-=,*=,/=,//=,%=,**=,
num = 50
num += 100
print(num)

# Comparison operators -> ==,!=,>,<,>=,<=
num1 = 2
num2 = 4

print ("numi is equal to num2 is :",num1==num2) 
print ("numi is equal to num2 is :",num1>=num2) 
print ("numi is equal to num2 is :",num1<=num2) 
print ("numi is equal to num2 is :",num1!=num2) 

# Logical operators -> and,or,not "# note the (==) always compared the two values and always give the boolean values "
a = True 
b = False

print ("True and Fales is :",a and b) #False
print (" False and False is :",b and b)#false 
print ("Fale and True is: ",b and a)#false
print ("True and True is :",a and a)#True 


# truth table of the or gate 
print ("True or Fales is :",a or b) #TRUE 
print (" False OR  False is :",b or b)#false 
print ("Fale and True is: ",b or  a)#True 
print ("True and True is :",a or a)#True 

# truth table of  the   not gate 
print (not(a))
