import sys
print('sys: ',sys.path)
# import config
from flask_app import config

from flask import Flask, jsonify
from sqlalchemy import create_engine, text 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#sqlalchemy for mariaDB
from sqlalchemy.orm import scoped_session, sessionmaker 
from sqlalchemy.ext.declarative import declarative_base



db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

        
    # blueprint
    # main_views.py에서 url 관리
    from .views import main_views
    app.register_blueprint(main_views.bp)    

    return app
