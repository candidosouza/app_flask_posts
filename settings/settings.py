import os
from flask import Flask


class Setting:
    """Classe para armazenamento das configurações do projeto"""

    __BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        """Inicializa as configurações da aplicação"""
        self.__env = os.environ
        self.__app = Flask(__name__)

    @property
    def env(self):
        return self.__env

    @classmethod
    def base_dir(cls):
        return cls.__BASE_DIR

    @property
    def app(self):
        return self.__app


setting = Setting()
# print(setting.env['DEBUG'])
