#!/usr/bin/env python
import socket
import pickle
import threading
import time
import cv2
import sys
from pygame.locals import *

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
color = False


def chunks(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]


def sendpic(name, abc):
    address = host, port = "127.0.0.1", 4005
    time.sleep(1)
    try:
        tcp_sock = socket.create_connection(address, timeout=10)
        tcp_sock.settimeout(None)
        # TODO: Finalizar thread e liberar porta quando o cliente desconectar
        while True:
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            fr = pickle.dumps(frame)
            list_chunks = list(chunks(fr, 46080))
            msg = tcp_sock.recv(1024)
            if msg.decode('UTF-8') == 'ready':
                if tcp_sock.send(bytes(str(sys.getsizeof(fr)), 'UTF-8')):
                    confirm = tcp_sock.recv(1024)
                    for n in list_chunks:
                        tcp_sock.send(n)
    except ConnectionRefusedError:
        tcp_sock = -1
    tcp_sock.close()
    cap.release()


def main():
    host = '127.0.0.1'
    tcp_port = 4004
    address = host, tcp_port
    sock = socket.socket()
    sock.bind(address)
    sock.listen(5)

    print("Server started...")
    while True:
        conn, addr = sock.accept()
        t = threading.Thread(
            target=sendpic, args=('SendPicture', 'abc'))
        t.start()
        print("Client connected. IP: ", str(addr))

        while conn:
            userresponse = conn.recv(1024)
            userresponse = userresponse.decode('UTF-8')
            if (userresponse != ''):
                print("Movimento: ", userresponse)
            if not userresponse:
                break
        print("Client desconnected.")


if __name__ == '__main__':
    main()
