from typing import List
import mysql.connector
from src.products.Product import Product

class ProductRepository:
    def __init__(self):
        pass    
    
    def save(self, products: List[Product]):
        cnx = mysql.connector.connect(user='root', password='toto',
                              host='127.0.0.1',
                              database='msi')
        cursor = cnx.cursor()
        for product in products:
            query = ("INSERT INTO products"
                 "(description, purchase_price, selling_price, quantity_stock, minimum_stock, date_added, product_type_id, supplier_id)"
                  "VALUES (%s, %s, %s, %s, %s, %s,%s,%s)")
            queryData= (product.GetDescription(), product.GetPurchaseprice(), product.GetSellingprice(), product.GetStock(), product.GetMinstock(), product.Getdate(), product.GetProducttype(), product.GetSupplierId() )
            cursor.execute(query, queryData)
            cnx.commit()
        cursor.close()
        cnx.close()
        
    def GetAllProducts(self):
        cnx = mysql.connector.connect(user='root', password='toto',
                              host='127.0.0.1',
                              database='msi')
        cursor = cnx.cursor()
        query = ("SELECT id, description, purchase_price, selling_price, quantity_stock, minimum_stock, date_added, product_type_id, supplier_id FROM products")
        cursor.execute(query)
        RequestResults = cursor.fetchall()
        result = list()
        
        for data in RequestResults:
            product = Product(data[0], data[1], data[2], data[3], data[5], data[6], data[7], data[8])
            product.addProductInStocks(data[4])
            result.append(product)
            
        for row in result:
            print("{}, {}, {}, {}, {}, {}, {}, {}, {}" .format(row.GetId(), row.GetDescription(), row.GetPurchaseprice(), row.GetSellingprice(), row.GetStock(), row.GetMinstock(), row.Getdate(), row.GetProducttypeid(), row.GetSupplierId()))
            