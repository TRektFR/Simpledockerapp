import os
from flask import Flask, render_template
import mysql.connector


class DBManager:
    def __init__(self, database="example", host="db", user="root"):
        self.connection = mysql.connector.connect(
            user="root", 
            password="mysql2022",
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()
    
    
    def query_countries_list(self):

        self.cursor.execute('Select * from countries')
        results = self.cursor.fetchall()
        return results

server = Flask(__name__)
conn = None

@server.route('/')
def index():
    global conn
    if not conn:
    	conn = DBManager()
    res = conn.query_countries_list()
    return render_template("index.html")

@server.route('/list')
def list():
    global conn
    if not conn:
    	conn = DBManager()
    res = conn.query_countries_list()
    response = ''
    for row in res:
    	response = response +"<div> {0},{1} </div>".format(row[0], row[1]) 
    return response
	



if __name__ == '__main__':
    server.run()
