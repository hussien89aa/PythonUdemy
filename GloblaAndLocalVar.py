
x=10 # global Var

def Show():
     print("x={}".format(x))

def main():
    # x=10 local var
    print("x={}".format(x))
    Show()
if __name__ == '__main__':main()