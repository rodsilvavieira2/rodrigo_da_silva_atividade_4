from flask import jsonify
from flask_restful import Resource, reqparse

from helpers.parse_data import parse_null_values, parse_args_to_tuple
from services.MarcaEquipamento import MarcaEquipamento


class MarcaEquipamentoInsertRoute(Resource):

    def post(self):
        param = reqparse.RequestParser()
        param.add_argument('nome_marca', type=str, required=True)

        args = param.parse_args()

        data = parse_args_to_tuple(
            args, ['nome_marca']
        )

        marcaEquipamento = MarcaEquipamento()

        result = marcaEquipamento.insert(data)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Dados insesidos com sucesso!"
                   }, 201


class MarcaEquipamentoListRoute(Resource):

    def get(self):
        marcaEquipamento = MarcaEquipamento()
        result = marcaEquipamento.select()

        if result:
            return jsonify(result)


class MarcaEquipamentoListByIdRoute(Resource):

    def get(self, id):
        marcaEquipamento = MarcaEquipamento()
        result = marcaEquipamento.select_by_id(id)

        if result:
            return jsonify(result)


class MarcaEquipamentoUpdateRoute(Resource):

    def put(self, id):
        param = reqparse.RequestParser()
        param.add_argument('nome_marca', type=str, required=True)

        args = param.parse_args()

        data = parse_null_values(args)

        marcaEquipamento = MarcaEquipamento()

        result = marcaEquipamento.update(data, id)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200


class MarcaEquipamentoDeleteRoute(Resource):
    def delete(self, id):
        marcaEquipamento = MarcaEquipamento()

        result = marcaEquipamento.delete(id)

        if result:
            return {}, 204
