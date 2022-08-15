import socket


class Server(object):
    def __init__(self, host = 'localhost', port = 2808) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        address = (host, port)

        self._socket.bind(address)
        self._socket.listen(1)
