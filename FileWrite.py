
def main():
    #Write to file
    out=open("test.txt","a")
    for i in range(5):
        inputToFile=input("enter string to write to file:")
        out.write("\n{}".format(inputToFile))
    out.close()



if __name__ == '__main__':main()
