import socket
from _thread import *
import sys

server = "104.22.6.107"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server started...")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break

            else:
                print("Received: " + str(reply))
                print("Sending: " + str(reply))

            conn.sendall(str.encode(reply))

        except:
            break
    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: " + str(addr))

    start_new_thread(threaded_client, (conn,))
