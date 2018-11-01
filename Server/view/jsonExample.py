from flask_restful import Resource
from flask import json, Response


class JsonExample(Resource):

    def get(self):

        out_data = {
                   "routes": [
                       {
                           "copyrights": "지도 데이터 ©2017 SK telecom",
                           "legs": [
                               {
                                   "end_address": "대한민국 서울특별시 서초구 양재2동 236 양재시민의숲",
                                   "start_address": "대한민국 서울특별시 용산구 용산동6가 455",

                                   "steps": [
                                       {
                                           "distance": {
                                               "text": "1.1 km",
                                               "value": 1138
                                           },
                                           "duration": {
                                               "text": "19분",
                                               "value": 1138
                                           },
                                           "html_instructions": "구반포역.심산문화센터까지 도보",
                                           "polyline": {
                                               "points": "_o}cFg}`fWh}@mQ"
                                           },
                                           "travel_mode": "WALKING"
                                       },
                                       {
                                           "distance": {
                                               "text": "7.8 km",
                                               "value": 7824
                                           },
                                           "duration": {
                                               "text": "19분",
                                               "value": 1116
                                           },
                                           "html_instructions": "버스 분당구.구미동행",
                                           "transit_details": {
                                               "arrival_stop": {
                                                   "name": "시민의숲.양재꽃시장"
                                               },
                                               "departure_stop": {
                                                   "name": "구반포역.심산문화센터"
                                               },
                                               "headsign": "분당구.구미동",
                                               "headway": 720,
                                               "num_stops": 12
                                           },
                                           "travel_mode": "TRANSIT"
                                       },
                                       {
                                           "distance": {
                                               "text": "0.3 km",
                                               "value": 254
                                           },
                                           "duration": {
                                               "text": "4분",
                                               "value": 254
                                           },
                                           "html_instructions": "대한민국 서울특별시 서초구 양재2동 236 양재시민의숲까지 도보",
                                           "travel_mode": "WALKING"
                                       }
                                   ]
                               }
                           ]
                       }
                   ],
                   "status": "OK"
               }

        return Response(
            json.dumps(out_data, ensure_ascii=False),
            200,
            content_type='application/json; charset=utf8'
        )
