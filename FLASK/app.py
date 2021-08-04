import sys
# print('sys: ',sys.path)
# import config
from flask_app import config

from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, text 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#sqlalchemy for mariaDB
from sqlalchemy.orm import scoped_session, sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

import os

print('등록된 경로 : ' ,dir())

SECRET_KEY = os.urandom(32)

db = SQLAlchemy()
migrate = Migrate()

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

print("Test",app)
app.config.from_object(config)
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)
migrate.init_app(app, db)

from flask_app import models
# blueprint 등록 : url경로 등록
from flask_app.views import main_views, theme_views
app.register_blueprint(main_views.bp)    
app.register_blueprint(theme_views.bp)


if __name__ == "__main__":
    app.run(debug = True)



def create_app():
    @app.route('/hello')
    def hello_pybo():
        print("app.register_blueprint(theme_views.bp)",app.register_blueprint(theme_views.bp))
        return 'Hello, Pybo!'
  
    return app