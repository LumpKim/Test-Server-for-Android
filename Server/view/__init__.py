from flask import Response, json


class Utility:

    def unicode_safe_json_dumps(cls, data, status_code=200, **kwargs):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf-8',
            **kwargs
        )