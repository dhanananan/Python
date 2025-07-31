# wap find the in a letter template given below with the name and date.
template = """"Dear {name},\nYour appointment is scheduled for {date}.\nThank you!"""
name = input("enter your name:")
date = input("enter the date:")
template = template.replace ("{name}", name)
template = template.replace ("{date}", date)
print(template)