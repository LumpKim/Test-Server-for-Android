from flask import jsonify
from datetime import datetime
from flask_restful import Resource
from server import started_time


class ServerInfo(Resource):

    def get(self):
        return jsonify({
            "servertime": datetime.now(),
            "runTime": datetime.now() - started_time
        }), 200
