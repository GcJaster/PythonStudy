class HandlerGET:
    def __init__(self, func) -> None:
        self.__func = func

    def __call__(self, request: dict) -> str or None:
        return f"GET: {self.__func(request)}" if request["method"] == "GET" else None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


if __name__ == '__main__':
    res = contact({"method": "POST", "url": "contact.html"})
    print(res)