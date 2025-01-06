from typing import List
import mysql.connector
from src.customers.Customer import Customer

class CustomerRepository:
    def __init__(self):
        pass
    
    def save(self, customers: List[Customer]):
        cnx = mysql.connector.connect(user='root', password='toto',
                              host='127.0.0.1',
                              database='msi')
        cursor = cnx.cursor()
        for customer in customers:
            query = ("INSERT INTO customers" 
                     "(name, address, phone, email)"
                     "VALUES(%s,%s,%s,%s)")
            queryData =(customer.GetName(), customer.GetAddress(), customer.GetPhone(), customer.GetEmail())
            cursor.execute(query, queryData)
            cnx.commit()
        cursor.close()
        cnx.close()
         
    def GetAllCustomers(self):  
    
        cnx = mysql.connector.connect(user='root', password='toto',
                                        host='127.0.0.1',
                                        database='msi')
        cursor = cnx.cursor()
        query=("SELECT id, name, address, phone, email FROM msi.customers")
        cursor.execute(query)
        requestResults = cursor.fetchall()
        result = list()
        
        for data in requestResults:
            customer = Customer(data[0], data[1], data[2], data[3], data[4])
            result.append(customer)
            
        for row in result:
            print("{}, {}, {}, {}, {}" .format(row.GetId(), row.GetName(), row.GetAddress(), row.GetPhone(), row.GetEmail()))
                
        cursor.close()
        cnx.close() 