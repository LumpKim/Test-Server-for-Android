from datetime import datetime
from flask_restful import Resource
from temp import started_time


class ServerInfo(Resource):

    def get(self):
        output = {
            "serverTime": str(datetime.now()),
            "runTime": str(datetime.now() - started_time)
        }
        return output, 200
