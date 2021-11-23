from flask_restful import HTTPException


class InternalServerError(HTTPException):
    pass


class NotFoundError(HTTPException):
    pass


class InsertError(HTTPException):
    pass


class UpdateError(HTTPException):
    pass


class DeleteError(HTTPException):
    pass


class SelectError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Erro de servidor interno.",
        "sucesso": False,
        "status": 500
    },
    "NotFoundError": {
        "message": "Nehum dado a ser exibido.",
        "sucesso": True,
        "status": 404
    },
    "InsertError": {
        "message": "Erro ao inserir dados",
        "sucesso": False,
        "status": 400
    },
    "UpdateError": {
        "message": "Erro em atualizar dados",
        "sucesso": False,
        "status": 400
    },
    "DeleteError": {
        "message": "Erro em deletar dados",
        "sucesso": False,
        "status": 400
    },
    "SelectError": {
        "message": "Erro em listar dados",
        "sucesso": False,
        "status": 400
    },
}
