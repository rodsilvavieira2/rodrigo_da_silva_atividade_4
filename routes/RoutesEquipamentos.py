from datetime import datetime

from flask import jsonify
from flask_restful import Resource, reqparse

from helpers.parse_data import parse_null_values, parse_args_to_tuple
from services.Equipamentos import Equipamentos


class EquipamentosInsertRoute(Resource):

    def post(self):
        param = reqparse.RequestParser()
        param.add_argument('nome_equipamento', type=str, required=True)
        param.add_argument('data_cadastro', type=str, required=True)
        param.add_argument('valor_equipamento', type=float, required=True)
        param.add_argument(
            'capacidade_armazenamento', type=float, required=True
        )
        param.add_argument('id_marcaequipamento',
                           type=int, required=True)
        param.add_argument('id_processador', type=int, required=True)
        param.add_argument('id_placavideo', type=int, required=True)
        param.add_argument('id_setor', type=int, required=True)

        args = param.parse_args()

        now = datetime.now()

        args.update({'created_at': now, 'updated_at': now})

        data = parse_args_to_tuple(
            args, [
                'nome_equipamento', 'data_cadastro', 'valor_equipamento',
                'capacidade_armazenamento', 'id_marcaequipamento',
                'id_processador', 'id_placavideo', 'id_setor',
                'created_at', 'updated_at'
            ]
        )

        equipamentos = Equipamentos()

        result = equipamentos.insert(data)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Dados insesidos com sucesso!"
                   }, 201


class EquipamentosListRoute(Resource):

    def get(self):
        equipamentos = Equipamentos()
        result = equipamentos.select()

        if result:
            return jsonify(result)


class EquipamentosListByIdRoute(Resource):

    def get(self, id):
        equipamentos = Equipamentos()
        result = equipamentos.select_by_id(id)

        if result:
            return jsonify(result)


class EquipamentosUpdateRoute(Resource):

    def put(self, id):
        param = reqparse.RequestParser()
        param.add_argument('nome_equipamento', type=str, required=False)
        param.add_argument('data_cadastro', type=str, required=False)
        param.add_argument('valor_equipamento', type=float, required=False)
        param.add_argument(
            'capacidade_armazenamento', type=float, required=False
        )
        param.add_argument('id_marcaequipamento', type=int, required=False)
        param.add_argument('id_processador', type=int, required=False)
        param.add_argument('id_placavideo', type=int, required=False)
        param.add_argument('id_setor', type=int, required=False)

        args = param.parse_args()

        now = datetime.now()

        args.update({'updated_at': now})

        data = parse_null_values(args)

        equipamentos = Equipamentos()

        result = equipamentos.update(data, id)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200


class EquipamentosDeleteRoute(Resource):
    def delete(self, id):
        equipamentos = Equipamentos()

        result = equipamentos.delete(id)

        if result:
            return {}, 204
