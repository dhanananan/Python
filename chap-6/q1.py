# wap a program to find the greater of four number enter by the user 

num1 =int(input("enter the first number :"))
num2=int(input("enter the second number :"))
num3 =int(input("enter the third  number :"))
num4 =int(input("enter the forth number :"))

if (num1 > num2 )and (num1>num3) and (num1>num4):
    print("print the num1 is greater ",num1)
elif(num2 >num1)and(num2 >num3 ) and (num2>num4):
    print("print the num2 is greater ",num2)
elif(num3>num1)and (num3>num2)and (num3>num4):
    print("print the num3 is greater",num3)
elif(num4>num1)and(num4>num2)and(num4>num3):
    print("print the num4 is greater",num4)
else:
    print("all number are equal")