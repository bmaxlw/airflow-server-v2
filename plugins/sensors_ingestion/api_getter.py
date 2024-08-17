import requests

class ApiGetter:

    @staticmethod
    def get_endpoint(endpoint: str) -> str:
        return requests.get(endpoint).text
