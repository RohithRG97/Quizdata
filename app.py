from flask import Flask, request, render_template
import string
import re
import os
import pypyodbc as odbc


app = Flask(__name__)

connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:freecloudsqlserver001.database.windows.net,1433;Database=DemoSQLServerDB;Uid=RohithGurram;Pwd={freecloudsqlserver@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
cnxn = odbc.connect(connection_string)


@app.route('/abc', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lon_min = request.form['lon_min']
        lon_max = request.form['lon_max']
        year_min = request.form['year_min']
        year_max = request.form['year_max']

        # Query the database
        cursor = cnxn.cursor()
        cursor.execute("SELECT STRCITY, STRSTATE, ZIPCODE, LAT, LON FROM walmartns WHERE LON BETWEEN ? AND ? AND YEAR BETWEEN ? AND ?", (lon_min, lon_max, year_min, year_max))
        results = cursor.fetchall()

        # Count the number of STRCITY for each STRSTATE
        cursor.execute("SELECT STRSTATE, COUNT(DISTINCT STRCITY) FROM walmartns WHERE LON BETWEEN ? AND ? AND YEAR BETWEEN ? AND ? GROUP BY STRSTATE", (lon_min, lon_max, year_min, year_max))
        counts = cursor.fetchall()

        return render_template('results.html', results=results, counts=counts)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
