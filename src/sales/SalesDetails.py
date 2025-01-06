class Saledetails:
    __saleid: int
    __productid: int
    __quantitysale: int
    __unitprice: int
    
    def __init__(self, sale_id, product_id, quantity_sale, unit_price):
        self.__saleid = sale_id
        self.__productid = product_id
        self.__quantitysale = quantity_sale
        self.__unitprice =unit_price

    def GetProductId(self):
        return self.__productid
    
    def GetSaleId(self):
        return self.__saleid
    
    def GetQuantity(self):
        return self.__quantitysale
    
    def GetUnitPrice(self):
        return self.__unitprice
    
    def GetAmount(self):
        return self.__quantitysale*self.__unitprice
    