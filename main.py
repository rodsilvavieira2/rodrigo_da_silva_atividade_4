from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from routes.RoutesEquipamentos import *
from routes.RoutesMarcaEquipamento import *
from routes.RoutesPlacaVideos import *
from routes.RoutesProcessadores import *
from routes.RoutesSetores import *

from error.error import errors

app = Flask(__name__)
api = Api(app, errors=errors)
CORS(app)

# Equipamentos routes

api.add_resource(EquipamentosInsertRoute, '/equipamentos')
api.add_resource(EquipamentosListRoute, '/equipamentos')
api.add_resource(EquipamentosListByIdRoute,
                 '/equipamentos/<int:id>')
api.add_resource(EquipamentosUpdateRoute,
                 '/equipamentos/<int:id>')
api.add_resource(EquipamentosDeleteRoute,
                 '/equipamentos/<int:id>')

# MarcaEquipamenots routes

api.add_resource(MarcaEquipamentoInsertRoute,
                 '/marca_equipamentos')
api.add_resource(MarcaEquipamentoListRoute,
                 '/marca_equipamentos')
api.add_resource(MarcaEquipamentoListByIdRoute,
                 '/marca_equipamentos/<int:id>')
api.add_resource(MarcaEquipamentoUpdateRoute,
                 '/marca_equipamentos/<int:id>')
api.add_resource(MarcaEquipamentoDeleteRoute,
                 '/marca_equipamentos/<int:id>')

# PlacaVideo routes

api.add_resource(PlacaVideoInsertRoute,
                 '/placa_video')
api.add_resource(PlacaVideoListRoute,
                 '/placa_video')
api.add_resource(PlacaVideoListByIdRoute,
                 '/placa_video/<int:id>')
api.add_resource(PlacaVideoUpdateRoute,
                 '/placa_video/<int:id>')
api.add_resource(PlacaVideoDeleteRoute,
                 '/placa_video/<int:id>')
# Processadores routes

api.add_resource(ProcessadoresInsertRoute,
                 '/processadores')
api.add_resource(ProcessadoresListRoute,
                 '/processadores')
api.add_resource(ProcessadoresListByIdRoute,
                 '/processadores/<int:id>')
api.add_resource(ProcessadoresUpdateRoute,
                 '/processadores/<int:id>')
api.add_resource(ProcessadoresDeleteRoute,
                 '/processadores/<int:id>')
# Setores routes

api.add_resource(SetoresInsertRoute,
                 '/setores')
api.add_resource(SetoresListRoute,
                 '/setores')
api.add_resource(SetoresListByIdRoute,
                 '/setores/<int:id>')
api.add_resource(SetoresUpdateRoute,
                 '/setores/<int:id>')
api.add_resource(SetoresDeleteRoute,
                 '/setores/<int:id>')

if __name__ == "__main__":
    app.run(port=4000)
