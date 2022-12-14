class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, route_cls):
        self.__path = path
        self.__route_cls = route_cls

    def __call__(self, func):
        return self.__route_cls.add_callback(self.__path, func)


def main() -> None:
    @Callback('/', Router)
    def index():
        return '<h1>Главная</h1>'

    route = Router.get('/')
    if route:
        ret = route()
        print(ret)


if __name__ == '__main__':
    main()