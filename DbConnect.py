import  sqlite3
db=sqlite3.connect("information.db")

def CreateTable():
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists Admin(ID integer primary key autoincrement, Name text,Age int)")
    db.commit()

def Add(Name,Age):
    db.row_factory=sqlite3.Row
    # Add records
    db.execute("insert into Admin(Name,Age) values(?,?)",(Name,Age))
    db.commit()
    print("Record is added")

def ListAdmins():
    cursor=db.execute("select * from Admin")
    for row in cursor:
        print("ID:{},Name:{},Age:{}".format(row["ID"],row["Name"],row["Age"]))

def DeleteRecord(ID):
    db.row_factory=sqlite3.Row
    # Add records
    db.execute("delete from Admin where ID={}".format(ID))
    db.commit()
    print("Record is deleted")
def UpdateRecord(ID,Age):
    db.row_factory=sqlite3.Row
    # Add records
    db.execute("update Admin set Age=? where ID=?",(Age,ID))
    db.commit()
    print("Record is Updated")



def main():
    CreateTable()
    while 1:
        IndexOp=int(input("\n===\nSelect Operation,"
                          "\n 1- Add\n"
                          "2- List Admins\n3- delete\n 4- update age\n 0- exit\n===\nIndex number:"))
        if(IndexOp==0):
            break;
        elif(IndexOp==1):
            Name=input("Enter name:")
            Age = int(input("Enter Age:"))
            Add(Name,Age)
        elif(IndexOp==2):
            ListAdmins()
        elif(IndexOp==3):
            ID=int(input("Enter ID to delete:"))
            DeleteRecord(ID)
        elif(IndexOp==4):
            ID= int(input("Enter person ID:"))
            Age = int(input("Enter new Age:"))
            UpdateRecord(ID,Age)


if __name__ == '__main__':main()
