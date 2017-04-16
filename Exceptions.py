
def main():
    try:
        x=int( input("enter number"))
        print(x+5)
    except ValueError:
        print(" value have to be interger")
if __name__ == '__main__':main()
