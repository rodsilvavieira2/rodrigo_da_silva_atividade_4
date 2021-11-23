from __future__ import annotations

from connection.Connection import Connection
from error.error import *


class PlacaVideo(Connection):

    def insert(self, values: tuple) -> bool | Exception:
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO tb_placavideo VALUES (null, %s, %s, %s, %s)"
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
                "SELECT * FROM tb_placavideo")
            result = cursor.fetchall()

            if not len(result):
                raise NotFoundError

            data = dict()
            for x in result:
                data.update({
                    x[0]: {
                        "id": x[0],
                        "nome_placa": x[1],
                        "modelo_placa": x[2],
                        "cuda_cores": x[3],
                        "memoria_video": x[4],
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
                f"SELECT * FROM tb_placavideo WHERE id = {id}")
            result = cursor.fetchone()

            if not result:
                raise NotFoundError

            data = dict()

            data.update(
                {
                    "id": result[0],
                    "nome_placa": result[1],
                    "modelo_placa": result[2],
                    "cuda_cores": result[3],
                    "memoria_video": result[4],
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
            sql = f"UPDATE tb_placavideo SET {data} WHERE id = {id}"
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
            sql = f"DELETE FROM tb_placavideo WHERE id = {id}"
            cursor.execute(sql)
            self.connection.commit()
            if not cursor.rowcount:
                raise DeleteError

            return True
        except DeleteError:
            raise DeleteError

        except Exception as e:
            raise InternalServerError
