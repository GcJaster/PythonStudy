class RenderList:
    def __init__(self, type_list: str) -> None:
        self.type_list = type_list if type_list in ('ul', 'ol') else 'ul'

    def __call__(self, items: list) -> str:
        new_list = '\n'.join([f"<li>{el}</li>" for el in lst])

        return f'<{self.type_list}>\n' \
               f'{new_list}\n' \
               f'</{self.type_list}>'


if __name__ == '__main__':
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    render = RenderList("el")
    html = render(lst)
    print(html)