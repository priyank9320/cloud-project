# home.py
from flask import Flask, request, render_template, jsonify
import time
import mysql.connector
import os
import json








app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_table():
    db_connection = mysql.connector.connect(host=os.environ["DB_HOST"], database=os.environ["DB_NAME"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
    query="select * from cloud_project.preprocess;"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    db_connection.close()

    return render_template("home.html",value=rows)



if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=5000)
