from typing import Callable, Dict, Tuple, Any, List

RouteKey = Tuple[str, str]

class FastAPI:
    def __init__(self, title: str = ""):
        self._routes: Dict[RouteKey, Callable] = {}

    def get(self, path: str):
        def decorator(func: Callable):
            self._routes[("GET", path)] = func
            return func
        return decorator

    def post(self, path: str):
        def decorator(func: Callable):
            self._routes[("POST", path)] = func
            return func
        return decorator

    @property
    def routes(self) -> Dict[RouteKey, Callable]:
        return self._routes
