class Car:
    def __init__(self,**kwargs):
        self._Data=kwargs

    def GetType(self):
        return self._Data["Type"]
    def GetModel(self):
        return self._Data["Model"]
    def GetPrice(self):
        return self._Data["Price"]
    def GetMilesDrive(self):
        return self._Data["MilesDrive"]
    def GetOwner(self):
        return self._Data["Owner"]

    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)



def main():
    myCar= Car(Type="BMW",Model=2015,Price=26000,MilesDrive=15,Owner="Hussein")
    CurrentPrice=myCar.GetCurrentPrice()
    print("{}'s Car, New price {}".format(myCar.GetOwner(),CurrentPrice))


    AlexCar= Car(Type="GMC",Model=2017,Price=28000,MilesDrive=5,Owner="Alex")
    CurrentPrice=AlexCar.GetCurrentPrice()
    print("{} 's Car, New price {}".format(AlexCar.GetOwner(),CurrentPrice))




if __name__ == '__main__':main()
