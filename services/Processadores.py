from __future__ import annotations

from connection.Connection import Connection
from error.error import *


class Processadores(Connection):

    def insert(self, values: tuple) -> bool | Exception:
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO tb_processadores VALUES" \
                  " (null, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)
            self.connection.commit()

            if not cursor.rowcount:
                raise InsertError

            return True
        except InsertError:
            raise InsertError

        except Exception as e:
            raise InternalServerError

    def select(self) -> bool | Exception | dict:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM tb_processadores")
            result = cursor.fetchall()

            if not len(result):
                raise NotFoundError

            data = dict()
            for x in result:
                data.update({
                    x[0]: {
                        "id": x[0],
                        "nome_processador": x[1],
                        "modelo_processador": x[2],
                        "arquitetura": x[3],
                        "clock": x[4],
                        "qtd_cores": x[5],
                        "qtd_threads": x[6],
                        "marca_processador": x[7]
                    }
                })
            return data
        except NotFoundError:
            raise NotFoundError

        except Exception as e:
            raise InternalServerError

    def select_by_id(self, id: int) -> bool | Exception | dict:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"SELECT * FROM tb_processadores WHERE id = {id}"
            )
            result = cursor.fetchone()

            if not result:
                raise NotFoundError

            data = dict()

            data.update(
                {
                    "id": result[0],
                    "nome_processador": result[1],
                    "modelo_processador": result[2],
                    "arquitetura": result[3],
                    "clock": result[4],
                    "qtd_cores": result[5],
                    "qtd_threads": result[6],
                    "marca_processador": result[7]
                }
            )
            return data
        except NotFoundError:
            raise NotFoundError

        except Exception as e:
            raise InternalServerError

    def update(self, data: str, id: int) -> bool | Exception:
        cursor = self.connection.cursor()
        try:
            sql = f"UPDATE tb_processadores SET {data} WHERE id = {id}"
            cursor.execute(sql)
            self.connection.commit()

            if not cursor.rowcount:
                raise UpdateError

            return True
        except UpdateError:
            raise UpdateError

        except Exception as e:
            raise InternalServerError

    def delete(self, id: int) -> bool | Exception:
        cursor = self.connection.cursor()
        try:
            sql = f"DELETE FROM tb_processadores WHERE id = {id}"
            cursor.execute(sql)
            self.connection.commit()
            if not cursor.rowcount:
                raise DeleteError

            return True
        except DeleteError:
            raise DeleteError

        except Exception as e:
            raise InternalServerError
