import socket
import subprocess


class Server(object):
    def __init__(
        self,
        host = 'localhost',
        port = 2808,
        password: str = None
    ) -> None:
        self._password = password

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        address = (host, port)

        self._socket.bind(address)
        self._socket.listen(1)

    def _wait_data(self, client: socket.socket) -> str:
        data = client.recv(1024)
        return data.decode()
