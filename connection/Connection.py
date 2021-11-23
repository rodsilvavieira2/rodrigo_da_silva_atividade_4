import mysql.connector

from error.error import InternalServerError


class Connection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="1234",
                database="atividade_flask"
            )
        except Exception as e:
            raise InternalServerError
