import datetime
DOB=input("Enter your DOB:")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
if(Age>=18):
    print("Your age is {} and you are Adult".format(Age))
if(Age<18):
    print("Your age is {} and you are not Adult".format(Age))
print("App is done")