from flask import jsonify
from flask_restful import Resource, reqparse

from helpers.parse_data import parse_null_values, parse_args_to_tuple
from services.Setores import Setores


class SetoresInsertRoute(Resource):

    def post(self):
        param = reqparse.RequestParser()
        param.add_argument('nome_setor', type=str, required=True)
        param.add_argument('gerente_setor', type=str, required=True)
        param.add_argument('sigla_setor', type=str, required=True)
        param.add_argument(
            'qtde_funcionarios', type=int, required=True
        )

        args = param.parse_args()

        data = parse_args_to_tuple(
            args, [
                'nome_setor', 'gerente_setor', 'sigla_setor',
                'qtde_funcionarios'
            ]
        )

        setores = Setores()

        result = setores.insert(data)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Dados insesidos com sucesso!"
                   }, 201


class SetoresListRoute(Resource):

    def get(self):
        setores = Setores()
        result = setores.select()

        return jsonify(result)


class SetoresListByIdRoute(Resource):

    def get(self, id):
        setores = Setores()
        result = setores.select_by_id(id)

        return jsonify(result)


class SetoresUpdateRoute(Resource):

    def put(self, id):
        param = reqparse.RequestParser()
        param.add_argument('nome_setor', type=str, required=False)
        param.add_argument('gerente_setor', type=str, required=False)
        param.add_argument('sigla_setor', type=str, required=False)
        param.add_argument(
            'qtde_funcionarios', type=int, required=False
        )

        args = param.parse_args()

        data = parse_null_values(args)

        setores = Setores()

        result = setores.update(data, id)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200


class SetoresDeleteRoute(Resource):
    def delete(self, id):
        setores = Setores()

        result = setores.delete(id)

        if result:
            return {}, 204
