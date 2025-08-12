from typing import Any, Dict

class Response:
    def __init__(self, status_code: int, json_data: Any):
        self.status_code = status_code
        self._json = json_data

    def json(self) -> Any:
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path: str, **kwargs) -> Response:
        func = self.app.routes[("GET", path)]
        return Response(200, func())

    def post(self, path: str, json: Any = None, **kwargs) -> Response:
        func = self.app.routes[("POST", path)]
        return Response(200, func(json))
