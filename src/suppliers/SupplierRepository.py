from typing import List
import mysql.connector
from src.suppliers.Supplier import Supplier

class SupplierRepository:
    def __init__(self):
        pass
    
    def save(self, suppliers: List[Supplier]):
        cnx = mysql.connector.connect(user='root', password='toto',
                                      host='127.0.0.1',
                                      database='msi')
        cursor= cnx.cursor()
        for supplier in suppliers:
            if self.checkifexist(supplier.GetName(), supplier.GetEmail()) == False:
                query =("INSERT INTO suppliers"
                        "(name, address, phone, email)"
                        "VALUES(%s,%s,%s,%s)")
                queryData =(supplier.GetName(), supplier.GetAddress(), supplier.GetPhone(), supplier.GetEmail())
                cursor.execute(query, queryData)
                cnx.commit()
                
        cursor.close()
        cnx.close()
        
    def checkifexist(self, name, email):
       cnx = mysql.connector.connect(user='root', password='toto',
                                      host='127.0.0.1',
                                      database='msi')
       cursor = cnx.cursor()
       query= ("SELECT * FROM suppliers where name = %s and email=%s") 
       queryData=(name, email)  
       cursor.execute(query, queryData)
       rows = cursor.fetchall()
       if len(rows) > 0:
           return True
       else:
           return False
       
    def GetAllSuppliers(self):
        
        cnx = mysql.connector.connect(user='root', password='toto',
                                        host='127.0.0.1',
                                        database='msi')
        cursor = cnx.cursor()
        query = ("SELECT id, name, address, phone, email FROM suppliers")
        cursor.execute(query)
        RequestResults = cursor.fetchall()
        result = list()
        
        for data in RequestResults:
            supplier = Supplier(data[0], data[1], data[2], data[3], data[4])
            result.append(supplier)
            
        for row in result:
            print("{}, {}, {}, {}, {}" .format(row.GetId(), row.GetName(), row.GetAddress(), row.GetPhone(), row.GetEmail()))
          
