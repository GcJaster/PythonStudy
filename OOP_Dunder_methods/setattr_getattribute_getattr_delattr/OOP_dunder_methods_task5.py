class SmartPhone:
    def __init__(self, model: str):
        self.model = model
        self.apps = []

    def add_app(self, app) -> None:
        if app.name not in [x.name for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app) -> None:
        self.apps.remove(app)


class AppVK:
    def __init__(self, name: str = "ВКонтакте") -> None:
        self.name = name


class AppYouTube:
    def __init__(self, memory_max: int, name: str = "YouTube") -> None:
        self.name = name
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list: dict, name: str = "Phone") -> None:
        self.name = name
        self.phone_list = phone_list


def main():
    sm = SmartPhone("Honor 1.0")
    sm.add_app(AppVK())
    sm.add_app(AppVK())  # второй раз добавляться не должно
    sm.add_app(AppYouTube(2048))
    for a in sm.apps:
        print(a.name)


if __name__ == '__main__':
    main()
