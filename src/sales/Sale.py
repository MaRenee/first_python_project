from datetime import date
from typing import List
from src.sales.SalesDetails import Saledetails


class Sale:
    __id: int
    __saledate: date
    __paymentmode: str
    __amount: int
    __status: str
    __customerid: int
    __saledetails: List[Saledetails]
        
    def __init__(self, id, sale_date, payment_mode, amount, status, customer_id, saledetails: List[Saledetails]):
        self.__id = id
        self.__saledate = sale_date
        self.__paymentmode = payment_mode
        self.__amount = amount
        self.__status = status
        self.__customerid = customer_id
        self.__saledetails = saledetails
    
    def GetAmount(self):
        amount = 0
        for saledetail in self.__saledetails:
            amount = amount + saledetail.GetAmount()
        return amount
    
    def GetSaleDate(self):
        return self.__saledate
    
    def GetPaymentMode(self):
        return self.__paymentmode
    
    def GetStatus(self):
        return self.__status
    
    def GetCustomerId(self):
        return self.__customerid
    
    def GetSaleDetails(self):
        return self.__saledetails
    
    def GetId(self):
        return self.__id