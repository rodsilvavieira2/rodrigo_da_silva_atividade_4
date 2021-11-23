from flask import jsonify
from flask_restful import Resource, reqparse

from helpers.parse_data import parse_null_values, parse_args_to_tuple
from services.Processadores import Processadores


class ProcessadoresInsertRoute(Resource):

    def post(self):
        param = reqparse.RequestParser()
        param.add_argument('nome_processador', type=str, required=True)
        param.add_argument('modelo_processador', type=str, required=True)
        param.add_argument('arquitetura', type=str, required=True)
        param.add_argument('clock', type=float, required=True)
        param.add_argument('qtd_cores', type=int, required=True)
        param.add_argument('qtd_threads', type=int, required=True)
        param.add_argument('marca_processador', type=int, required=True)

        args = param.parse_args()

        data = parse_args_to_tuple(
            args, [
                'nome_processador', 'modelo_processador', 'arquitetura',
                'clock', 'qtd_cores', 'qtd_threads', 'marca_processador'
            ]
        )

        processadores = Processadores()

        result = processadores.insert(data)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Dados insesidos com sucesso!"
                   }, 201


class ProcessadoresListRoute(Resource):

    def get(self):
        processadores = Processadores()
        result = processadores.select()

        if result:
            return jsonify(result)


class ProcessadoresListByIdRoute(Resource):

    def get(self, id):
        processadores = Processadores()
        result = processadores.select_by_id(id)

        if result:
            return jsonify(result)


class ProcessadoresUpdateRoute(Resource):

    def put(self, id):
        param = reqparse.RequestParser()
        param.add_argument('nome_processador', type=str, required=False)
        param.add_argument('modelo_processador', type=str, required=False)
        param.add_argument('arquitetura', type=str, required=False)
        param.add_argument('clock', type=float, required=False)
        param.add_argument('qtd_cores', type=int, required=False)
        param.add_argument('qtd_threads', type=int, required=False)
        param.add_argument('marca_processador', type=int, required=False)

        args = param.parse_args()

        data = parse_null_values(args)

        processadores = Processadores()

        result = processadores.update(data, id)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200


class ProcessadoresDeleteRoute(Resource):
    def delete(self, id):
        processadores = Processadores()

        result = processadores.delete(id)

        if result:
            return {}, 204
