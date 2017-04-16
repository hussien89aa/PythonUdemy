import datetime

def main():
    #main code function
    DOB=input("Enter your DOB:")
    CurrentYear=datetime.datetime.now().year
    Age=CurrentYear-int(DOB)
    print("Your age is {}".format(Age))




if __name__ == '__main__':main()
