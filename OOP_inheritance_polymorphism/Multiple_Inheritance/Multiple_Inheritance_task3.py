from typing import Dict


class RetriveMixin:
    def get(self, request: dict) -> str:
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request: dict) -> str:
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request: dict) -> str:
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: Dict[str, str]) -> str:
        if request.get('method') not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        else:
            """Getting a reference to a method by name and returning a request """
            method_request = request.get('method').lower()
            return getattr(self, method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )


if __name__ == '__main__':
    view = DetailView()
    html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
    print(html)  # GET: https://stepik.org/course/116336/