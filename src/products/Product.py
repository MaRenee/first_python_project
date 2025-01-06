from datetime import  datetime 
class Product:
    __description: int
    __purchaseprice: int
    __sellingprice: int
    __stock : int
    __minstock: int
    __date: datetime
    __producttypeid : int
    __supplierid: int
    __id: int
    
    def __init__(
                self, 
                id: int, 
                description: str, 
                purchaseprice: int, 
                sellingprice: int, 
                minstock: int, 
                date: datetime, 
                producttypeid: int,
                supplierid: int) :
        self.__id = id
        self.__description= description
        self.__purchaseprice = purchaseprice
        self.__sellingprice = sellingprice
        self.__minstock = minstock
        self.__date = date
        self.__producttypeid = producttypeid
        self.__supplierid = supplierid
        self.__stock = 0
    
    def GetId(self):
        return self.__id
    
    def GetDescription(self):
        return self.__description
    
    def GetPurchaseprice(self):
        return self.__purchaseprice
    
    def GetSellingprice(self):
        return self.__sellingprice
    
    def addProductInStocks(self, quantity):
        self.__stock += quantity

    def removeProductInStocks(self, quantity):
            self.__stock -= quantity

    def GetStock(self):
        return self.__stock
    
    def GetMinstock(self):
        return self.__minstock
    
    def Getdate(self):
        return self.__date
    
    def GetProducttypeid(self):
        return self.__producttypeid
    
    def GetSupplierId(self):
        return self.__supplierid
    