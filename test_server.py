#!/usr/bin/env python
import socket


def main():
    address = '127.0.0.1', 4004
    sock = socket.socket()
    sock.bind(address)
    sock.listen(5)

    print("Server started...")

    while True:
        conn, addr = sock.accept()
        print("Client connected. IP: ", str(addr))
        while conn:
            userresponse = conn.recv(1024)
            userresponse = userresponse.decode('UTF-8')
            if (userresponse != ''):
                print("Movimento: ", userresponse)

if __name__ == '__main__':
    main()
