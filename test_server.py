#!/usr/bin/env python
import socket
import cv2
import threading
import numpy
import sys

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
color = False


def sendpic(name):
    address = host, port = "127.0.0.1", 4005
    sock = socket.socket()
    sock.bind(address)
    sock.listen(5)

    while(True):
        ret, frame = cap.read()
        if not color:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = numpy.rot90(frame)
        fr = frame.tostring()
    sock.close()
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
        # t = threading.Thread(
        #     target=sendpic, args=('SendPicThread'))
        # t.start()
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
