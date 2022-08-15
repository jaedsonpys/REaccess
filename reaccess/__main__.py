import argeasy

from . import server
from . import client
from .__init__ import __version__


def main():
    parser = argeasy.ArgEasy(
        project_name='REaccess',
        description='Execute commands on another machine remotely.',
        version=__version__
    )

    parser.add_argument('server', 'Start server', action='store_true')
    parser.add_argument('client', 'Start client', action='store_true')

    parser.add_flag('--host', 'Set the connection host')
    parser.add_flag('--port', 'Set the connection port')
