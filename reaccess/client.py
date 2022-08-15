import socket


class Client(object):
    def __init__(self, host = 'localhost', port = 2808) -> None:
        address = (host, port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(address)

    def required_password(self) -> bool:
        connect_info = self._socket.recv(1024)
        return connect_info == 'required_password'
