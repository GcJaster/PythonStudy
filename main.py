def main():
    from Router import Router, Server, Data

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


