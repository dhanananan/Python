# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

# n =int(input("enter the number :"))
# for i in range(1,n):
#     if (i==2):
#         for i in range (i, n+1):
            
#     for i in range(1, n+1):
#         print ("*", end="") 
#     print("")
n =int(input("enter the number :"))
for i in range(1,n+1):
    print("*" ,end = "  ")
print("")
for i in range (1,n-1):
    for i in range (1, n+1):
        if (i == 1 or i == n):
            print("*", end ="  ")
        else:
            print(" " ,end ="  ")
    print(" ")
for i in range(1,n+1):
    print("*" ,end = "  ")
print("")
    
    
  

 