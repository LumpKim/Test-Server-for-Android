from flask_restful import Api
from creappate import create_app
from datetime import datetime

app = create_app()
api = Api(app)

access_count = 0
started_time = datetime.now()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
