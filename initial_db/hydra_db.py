import cx_Oracle
import os

class HydraDB:
    """
    Подключение к БД Hydra
    """

    def connect(self):
        connect = cx_Oracle.connect('YOUR_LOGIN', 'YOUR_PASSWORD', 'SERVER/hydra')  
        return connect.cursor()

