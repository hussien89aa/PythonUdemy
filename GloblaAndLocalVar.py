
x=10 #Global var
def Show():
     global x
     print(x)

def main():
    global x
    print("x={}".format(x))
    Show()
if __name__ == '__main__':main()