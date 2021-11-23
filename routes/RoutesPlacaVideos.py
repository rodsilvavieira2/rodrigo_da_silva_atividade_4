from flask import jsonify
from flask_restful import Resource, reqparse

from helpers.parse_data import parse_null_values, parse_args_to_tuple
from services.Placavideo import PlacaVideo


class PlacaVideoInsertRoute(Resource):

    def post(self):
        param = reqparse.RequestParser()
        param.add_argument('nome_placa', type=str, required=True)
        param.add_argument('modelo_placa', type=str, required=True)
        param.add_argument('cuda_cores', type=int, required=True)
        param.add_argument(
            'memoria_video', type=float, required=True
        )

        args = param.parse_args()

        data = parse_args_to_tuple(
            args, [
                'nome_placa', 'modelo_placa', 'cuda_cores',
                'memoria_video'
            ]
        )

        placaVideo = PlacaVideo()

        result = placaVideo.insert(data)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Dados insesidos com sucesso!"
                   }, 201


class PlacaVideoListRoute(Resource):

    def get(self):
        placaVideo = PlacaVideo()
        result = placaVideo.select()

        if result:
            return jsonify(result)


class PlacaVideoListByIdRoute(Resource):

    def get(self, id):
        placaVideo = PlacaVideo()
        result = placaVideo.select_by_id(id)

        if result:
            return jsonify(result)


class PlacaVideoUpdateRoute(Resource):

    def put(self, id):
        param = reqparse.RequestParser()
        param.add_argument('nome_placa', type=str, required=False)
        param.add_argument('modelo_placa', type=str, required=False)
        param.add_argument('cuda_cores', type=int, required=False)
        param.add_argument(
            'memoria_video', type=float, required=False
        )

        args = param.parse_args()

        data = parse_null_values(args)

        placaVideo = PlacaVideo()

        result = placaVideo.update(data, id)

        if result:
            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200


class PlacaVideoDeleteRoute(Resource):
    def delete(self, id):
        placaVideo = PlacaVideo()

        result = placaVideo.delete(id)

        if result:
            return {}, 204
