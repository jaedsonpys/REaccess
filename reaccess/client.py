import socket


class Client(object):
    def __init__(self, host = 'localhost', port = 2808) -> None:
        address = (host, port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(address)
