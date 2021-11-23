from __future__ import annotations

from connection.Connection import Connection
from error.error import *


class Equipamentos(Connection):

    def insert(self, values: tuple) -> bool | Exception:
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO tb_equipamentos VALUES" \
                  " (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)
            self.connection.commit()

            if not cursor.rowcount:
                raise InsertError

            return True
        except NotFoundError:
            raise NotFoundError

        except Exception as e:
            raise InternalServerError

    def select(self) -> bool | Exception | dict:
        cursor = self.connection.cursor()
        try:
            sql = "SELECT * FROM tb_equipamentos as e" \
                  " JOIN tb_processadores as p ON e.id_processador = p.id" \
                  " JOIN tb_setores as s ON e.id_setor = s.id" \
                  " JOIN tb_placavideo as v ON e.id_placavideo = v.id" \
                  " JOIN tb_marcaequipamento as m" \
                  " ON e.id_marcaequipamento = m.id"

            cursor.execute(sql)
            result = cursor.fetchall()

            if not len(result):
                raise NotFoundError

            data = dict()
            for x in result:
                data.update({
                    x[0]: {
                        "id": x[0],
                        "nome_equipamento": x[1],
                        "data_cadastro": x[2],
                        "valor_equipamento": x[3],
                        "capacidade_armazenamento": x[4],
                        "created_at": x[9],
                        "updated_at": x[10],
                        "nome_processador": x[12],
                        "modelo_processador": x[13],
                        "arquitetura": x[14],
                        "clock": x[15],
                        "qtd_cores": x[16],
                        "qtd_threads": x[17],
                        "marca_processador": x[18],
                        "nome_setor": x[20],
                        "gerente_setor": x[21],
                        "sigla_setor": x[22],
                        "qtde_funcionarios": x[23],
                        "nome_placa": x[25],
                        "modelo_placa": x[26],
                        "cuda_cores": x[27],
                        "memoria_video": x[28],
                        "nome_marca": x[30]
                    }
                })
            return data
        except NotFoundError:
            raise NotFoundError

        except Exception as e:
            return e

    def select_by_id(self, id: int) -> bool | Exception | dict:
        cursor = self.connection.cursor()

        sql = "SELECT * FROM tb_equipamentos as e" \
              " JOIN tb_processadores as p ON e.id_processador = p.id" \
              " JOIN tb_setores as s ON e.id_setor = s.id" \
              " JOIN tb_placavideo as v ON e.id_placavideo = v.id" \
              " JOIN tb_marcaequipamento as m" \
              " ON e.id_marcaequipamento = m.id" \
              f" WHERE e.id = {id}"

        try:
            cursor.execute(sql)
            result = cursor.fetchone()

            if not result:
                raise NotFoundError

            data = dict()

            data.update(
                {
                    "id": result[0],
                    "nome_equipamento": result[1],
                    "data_cadastro": result[2],
                    "valor_equipamento": result[3],
                    "capacidade_armazenamento": result[4],
                    "created_at": result[9],
                    "updated_at": result[10],
                    "nome_processador": result[12],
                    "modelo_processador": result[13],
                    "arquitetura": result[14],
                    "clock": result[15],
                    "qtd_cores": result[16],
                    "qtd_threads": result[17],
                    "marca_processador": result[18],
                    "nome_setor": result[20],
                    "gerente_setor": result[21],
                    "sigla_setor": result[22],
                    "qtde_funcionarios": result[23],
                    "nome_placa": result[25],
                    "modelo_placa": result[26],
                    "cuda_cores": result[27],
                    "memoria_video": result[28],
                    "nome_marca": result[30]
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
            sql = f"UPDATE tb_equipamentos SET {data} WHERE id = {id}"
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
            sql = f"DELETE FROM tb_equipamentos WHERE id = {id}"
            cursor.execute(sql)
            self.connection.commit()
            if not cursor.rowcount:
                raise DeleteError

            return True
        except DeleteError:
            raise DeleteError

        except Exception as e:
            raise InternalServerError
