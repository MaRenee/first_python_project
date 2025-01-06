import csv

import mysql.connector


file_path = ".\data\\customers.csv"
with open(file_path, 'r') as file:
    filecontent = csv.reader(file)
    
    cnx = mysql.connector.connect(user='root', password='toto',
                                host='127.0.0.1',
                                database='msi')
    cursor = cnx.cursor()
    for row in filecontent:

        # Vérification si le client existe déjà
          check_query = ("SELECT COUNT(*) FROM customers WHERE name = %s AND email = %s")
          queryData = (row[0], row[3])
          cursor.execute(check_query, queryData)
          result = cursor.fetchall()
          
    if result == 0:  # Si le client n'existe pas
         query = ("INSERT INTO customers" 
                     "(address, name, phone, email)"
                     "VALUES(%s,%s,%s,%s)")
         queryData = (row[1], row[0], row[2], row[3])
         cursor.execute(query, queryData)
         cnx.commit()
    else:
            print(f"Client déjà existant : {row[0]}, {row[3]}")
    
    cursor.close()
    cnx.close() 
    
 
    

    
    
        