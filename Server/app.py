# creappate.py makes app

from flask import Flask
from flask_restful import Api
from view.serverInfo import ServerInfo
from view.jsonExample import JsonExample


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ServerInfo, '/server')
    api.add_resource(JsonExample, '/json')

    return app
