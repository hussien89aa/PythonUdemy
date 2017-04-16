class User:
    def __init__(self,userName,age):
        self._UserName=userName
        self._Age=age
    def GetUserName(self):
        return self._UserName
    def GetAge(self):
        return self._Age


def main():
    u1=User("Hussein",26)
    print(u1.GetUserName())
    u2=User("Jena",2)
    print(u2.GetUserName())

if __name__ == '__main__':main()
