import socket
from server import PORT, DATA_PACKAGE_SIZE, action

sock = socket.socket()
sock.connect(('localhost', PORT))
messages = action
sock.send(messages.encode("utf-8"))
# sock.recv(DATA_PACKAGE_SIZE)