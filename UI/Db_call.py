from Class_DbConnect import DBConnect

def main():
    dbconnect= DBConnect()
    while 1:
        IndexOp=int(input("\n===\nSelect Operation,"
                          "\n 1- Add\n"
                          "2- List Admins\n3- delete\n 4- update age\n 0- exit\n===\nIndex number:"))
        if(IndexOp==0):
            break;
        elif(IndexOp==1):
            Name=input("Enter name:")
            Age = int(input("Enter Age:"))
            dbconnect.Add(Name,Age)
        elif(IndexOp==2):
            dbconnect.ListAdmins()
        elif(IndexOp==3):
            ID=int(input("Enter ID to delete:"))
            dbconnect.DeleteRecord(ID)
        elif(IndexOp==4):
            ID= int(input("Enter person ID:"))
            Age = int(input("Enter new Age:"))
            dbconnect.UpdateRecord(ID,Age)


if __name__ == '__main__':main()
