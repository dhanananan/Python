# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
#take marks as an input from the user.

sub1 =int(input("enter the marks : "))
sub2 =int(input("enter the marks : "))
sub3  =int(input("enter the marks : "))

total_percentage =((sub1 +sub2+sub3)*100)/300
if(total_percentage >= 40 ):
    print("your student is pass")
else:
    print("you are fail")
print("the total percentage is",total_percentage,"%"     )
    