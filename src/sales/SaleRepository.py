import mysql.connector
from src.sales.Sale import Sale
from src.sales.SalesDetails import Saledetails

class SaleRepository:
    def __init__(self):
        pass
    
    def save(self, sale: Sale):
       cnx = mysql.connector.connect(user='root', password='toto',
                                     host='127.0.0.1',
                                     database='msi') 
       cursor = cnx.cursor()
       query =("INSERT INTO Sales" 
                   "(sale_date, payment_mode, amount, status, customer_id)"
                   "VALUES(%s,%s,%s,%s,%s)")
       queryData  = (sale.GetSaleDate(), sale.GetPaymentMode(), sale.GetAmount(), sale.GetStatus(), sale.GetCustomerId())
       cursor.execute(query, queryData)
       saleId = cursor.lastrowid
       
       for saledetail in sale.GetSaleDetails():
          saledetailsquery = ("INSERT INTO sales_details"
                              "(sale_id, product_id, quantity_sale, unit_price, amount)"
                              "VALUES(%s,%s,%s,%s,%s)")
           
          saledetailsqueryData = (saleId, saledetail.GetProductId(), saledetail.GetQuantity(), saledetail.GetUnitPrice(), saledetail.GetAmount())
          cursor.execute(saledetailsquery, saledetailsqueryData)
       cnx.commit()
       
       cursor.close()
       cnx.close()
       
    
       
    