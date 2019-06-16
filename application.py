from flask import Flask, render_template,request
import pyodbc
import os
application = app = Flask(__name__)

#port = int(os.getenv("VCAP_APP_PORT", '5000'))
# port = os.getenv("VCAP_APP_PORT")




server = 'mysqlserversuchitra.database.windows.net'
database = 'assignment3'
username = 'azureuser'
password = 'Geetha1963@'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)


@app.route('/')
def home():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM people")
    row = cursor.fetchall()
    #return render_template('home.html', data=row)
    return render_template('people.html', data=row)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run('127.0.0.1',debug=True)

    #app.run(host='0.0.0.0', port=port)

   #app.run(debug=True)

    #app.run(host='127.0.0.1', port=port)
