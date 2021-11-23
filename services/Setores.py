from __future__ import annotations

from connection.Connection import Connection
from error.error import *


class Setores(Connection):

    def insert(self, values: tuple) -> bool | Exception:
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO tb_setores VALUES (null, %s, %s, %s, %s)"
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
                "SELECT * FROM tb_setores"
            )
            result = cursor.fetchall()

            if not len(result):
                raise NotFoundError

            data = dict()
            for x in result:
                data.update({
                    x[0]: {
                        "id": x[0],
                        "nome_setor": x[1],
                        "gerente_setor": x[2],
                        "sigla_setor": x[3],
                        "qtde_funcionarios": int(x[4]),
                    }
                })
            return data
        except NotFoundError:
            raise NotFoundError

        except Exception as e:
            raise InternalServerError

    def select_by_id(self, setor_id: int) -> bool | Exception | dict:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"SELECT * FROM tb_setores WHERE id = {setor_id}")
            result = cursor.fetchone()

            if not result:
                raise NotFoundError

            data = dict()

            data.update(
                {
                    "id": result[0],
                    "nome_setor": result[1],
                    "gerente_setor": result[2],
                    "sigla_setor": result[3],
                    "qtde_funcionarios": result[4],
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
            sql = f"UPDATE tb_setores SET {data} WHERE id = {id}"
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
            sql = f"DELETE FROM tb_setores WHERE id = {id}"
            cursor.execute(sql)
            self.connection.commit()

            if not cursor.rowcount:
                raise DeleteError

            return True
        except DeleteError:
            raise DeleteError

        except Exception as e:
            raise InternalServerError
