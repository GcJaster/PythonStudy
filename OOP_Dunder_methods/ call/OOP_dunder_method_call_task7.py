class Handler:
    def __init__(self, methods=("GET")) -> None:
        self.methods = methods

    def get(self, func, request, *args, **kwargs) -> str:
        return "GET: " + func(request)

    def post(self, func, request, *args, **kwargs) -> str:
        return "POST: " + func(request)

    def __call__(self, func):
        def wrapper(request, *args, **kwargs) -> str:
            method = "get"
            if "method" in request.keys():
                method = request["method"]
            if method in self.methods:
                return self.__getattribute__(method.lower())(func, request)
        return wrapper


@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


if __name__ == '__main__':
    print(contact({"method": "POST", "url": "contact.html"}))
