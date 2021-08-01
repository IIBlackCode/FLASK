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
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    
    # sqlite Ver
    # app.config.from_pyfile("config.py")

    # MariaDB Ver
    
    


    '''
    database = create_engine(app.config['DB_URL'], encoding='utf-8', max_overflow=0)
    app.database = database
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=database))
    Base = declarative_base() 
    Base.query = db_session.query_property() 
    @app.route('/test_db', methods=['GET'])
    def test_db():
        
        row = app.database.execute(text(""" SELECT * FROM userboard; """)).fetchall()
        print(type(row))
        print(row)
        return 'success'
    '''
        
    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)    

    return app
