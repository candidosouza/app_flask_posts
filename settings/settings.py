import os
import sqlite3


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Setting:
    """Classe para armazenamento das configurações do projeto"""

    __BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        """Inicializa as configurações da aplicação"""
        self.__env = os.environ
        self.__app = Flask(__name__)
        self.__db = SQLAlchemy(self.__app)

    @property
    def env(self):
        return self.__env

    @classmethod
    def base_dir(cls):
        return cls.__BASE_DIR

    @property
    def app(self):
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = self.__env['SQLALCHEMY_DATABASE_URI']
        return self.__app
    
    @property
    def db(self):
        return self.__db


setting = Setting()
# print(setting.env['DEBUG'])
