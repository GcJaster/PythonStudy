class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip


class Server:
    __list_ip = count(1)

    def __init__(self) -> None:
        self.buffer = list()
        self.ip = self.create_ip()
        self.__router = None

    @classmethod
    def create_ip(cls) -> int:
        """Return new Server-IP"""
        return next(cls.__list_ip)

    def send_data(self, data) -> None:
        """Send data to"""
        self.__router.buffer.append(data)

    def get_data(self) -> List[Data]:
        """Return list of data and clear buffer"""
        res = self.buffer
        self.buffer = list()
        return res

    def get_ip(self) -> int:
        """Return self IP"""
        return self.ip

    def link(self, router: object) -> None:
        """Link server to router"""
        self.__router = router


class Router:
    def __init__(self) -> None:
        self.__servers = dict()
        self.buffer = list()

    def link(self, server: Server) -> None:
        """Connect server to Router"""
        if server.ip not in self.__servers:
            server.link(router=self)
            self.__servers[server.ip] = server

    def unlink(self, server) -> None:
        """Unlink server from Router"""
        self.__servers.pop(server)

    def send_data(self) -> None:
        """Send data from router's buffer to server's buffer"""
        for data_obj in self.buffer:
            self.__servers[data_obj.ip].buffer.append(data_obj)


def main():
    from typing import List
    from itertools import count

    router = Router()
    sv_from = Server()
    router.link(sv_from)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    router.send_data()
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    print(sv_from.get_data())
    print(sv_to.get_data())


if __name__ == "__main__":
    main()


