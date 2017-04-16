class Car:
    def __init__(self,type,model,price,milesDrive,owner):
        self._Type=type
        self._Model=model
        self._Price=price
        self._MilesDrive=milesDrive
        self._Owner=owner

    def GetType(self):
        return self._Type
    def GetModel(self):
        return self._Model
    def GetPrice(self):
        return self._Price
    def GetMilesDrive(self):
        return self._MilesDrive
    def GetOwner(self):
        return self._Owner

    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)



def main():
    myCar= Car("BMW",2015,26000,15,"Hussein")
    CurrentPrice=myCar.GetCurrentPrice()
    print("{}'s Car, New price {}".format(myCar.GetOwner(),CurrentPrice))


    AlexCar= Car("GMC",2017,28000,5,"Alex")
    CurrentPrice=AlexCar.GetCurrentPrice()
    print("{} 's Car, New price {}".format(AlexCar.GetOwner(),CurrentPrice))




if __name__ == '__main__':main()
