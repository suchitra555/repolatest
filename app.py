import pyodbc
server = 'mysqlserversuchitra.database.windows.net'
database = 'assignment3'
username = 'azureuser'
password = 'Geetha1963@'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM people")
row = cursor.fetchall()
while row:
    print (str(row[0]) + " " + str(row[1]))
    # row = cursor.fetchall()