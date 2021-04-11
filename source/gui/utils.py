import socket

from server import app


def share_screen(port=3535):
    host = socket.gethostbyname(socket.gethostname())
    app.run(host=host, port=port)
