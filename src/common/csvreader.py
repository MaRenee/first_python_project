
import csv
import datetime
from src.customers.Customer import Customer
from src.products.Product import Product
from src.suppliers.Supplier import Supplier
from src.sales.Sale import Sale

class CsvReader:
    def __init__(self):
        pass
    
    def readCustomerFileData(self):
         file_path = "  .\\..\\data\\customers.csv"
         with open(file_path, 'r') as file:
           fileContent = csv.reader(file)
           result = list()
           for row in fileContent:
              customer = Customer(
                 row[0], 
                 row[1], 
                 row[2], 
                 row[3])
              result.append(customer)
           return result 
      
    def readProductFileData(self):
         file_path = " .\\..\\data\\products.csv"
         
         with open(file_path, 'r') as file:
           fileContent = csv.reader(file)
           products = list()
           for row in fileContent:
              content = row[0]
              elements = content.split(';')
              product = Product(
                           elements[0], 
                           int(elements[1]), 
                           int(elements[2]), 
                           int(elements[4]), 
                           datetime.datetime.strptime(elements[5], '%Y-%m-%d'), 
                           int(elements[6]), 
                           int(elements[7])
                        )
              
              product.addProductInStocks(int(elements[3]))
              
              products.append(product)
           return products
        
    def readSupplierFileData(self):
       file_path = "  .\\..\\data\\suppliers.csv"
       with open(file_path, 'r') as file:
          filecontent = csv.reader(file)
          result = list()
          for row in filecontent:
             supplier = Supplier(
                row[0],
                row[1],
                row[2],
                row[3])
             result.append(supplier)
          return result
             
    def readSaleFileData(self):
       file_path = ".\\data\\sales.csv"
       with open(file_path, 'r') as file:
          filecontent = csv.reader(file)
          result = list()
          for row in filecontent:
             sale = Sale(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4])
             result.append(sale)
          return result
      