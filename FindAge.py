import datetime
DOB=input("Enter your DOB:")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
print("Your age is {}".format(Age))