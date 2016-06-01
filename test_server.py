#!/usr/bin/env python
import socket


def main():
    address = '127.0.0.1', 4004
    sock = socket.socket()
    sock.bind(address)
    sock.listen(5)

    print("server started")

    while True:
        c, addr = sock.accept()
        print("Client connected. IP: ", str(addr))


if __name__ == '__main__':
    main()
