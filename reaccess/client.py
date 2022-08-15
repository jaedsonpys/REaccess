import socket


class Client(object):
    def __init__(self, host = 'localhost', port = 2808) -> None:
        address = (host, port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(address)

    def required_password(self) -> bool:
        connect_info = self._socket.recv(1024)
        return connect_info == 'required_password'

    def check_password(self, password: str) -> bool:
        self._socket.send(password.encode())
        result = self._socket.recv(1024)
        return result == 'logged'

    def send_command(self, command: str) -> None:
        self._socket.send(command.encode())
        result = self._socket.recv(1024)

        while result != 'finish':
            print(result)
            result = self._socket.recv(1024)
