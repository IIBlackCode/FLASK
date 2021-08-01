import os
import pymysql

BASE_DIR = os.path.dirname(__file__)
basedir = os.path.abspath(BASE_DIR)

db = {
        'user': 'root',
        'password': '41632',
        'host': '49.50.166.134',
        'port': '3306',
        'database': 'Flask_Project'}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = DB_URL
print(DB_URL)
SQLALCHEMY_TRACK_MODIFICATIONS = False


    
    