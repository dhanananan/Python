# wap to input the 8 number from the user and display the unique (once)

s = set()

user1 = int(input("enter the first number: "))
s.add(user1)
user2 = int(input("enter the second number: "))
s.add(user2)
user3 = int(input("enter the third number: "))
s.add(user3)
user4 = int(input("enter the fourth number: "))
s.add(user4)
user5 = int(input("enter the fifth number: "))
s.add(user5)
user6 = int(input("enter the  sirth number: "))
s.add(user6)
user7 = int(input("enter the seventh number: "))
s.add(user7)
user8 = int(input("enter the eighth number: "))
s.add(user8)

print(s)
#output {2, 3, 5, 6, 7}
