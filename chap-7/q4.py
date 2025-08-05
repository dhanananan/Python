# Write a program to find the sum of first n natural numbers using while loop.

n =int(input("Enter the number of terms: "))
count = 0
for i in range(1, n + 1):
   if(n%i == 0):
      count += 1
I
if(count == 2):
    print(f"{n} is a prime number")
else:
    print (f"{n} is not a prime number")