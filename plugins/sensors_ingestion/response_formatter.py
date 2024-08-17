import json

class ResponseFormatter:

    @staticmethod
    def format_response(response: str):
        return json.loads(response)