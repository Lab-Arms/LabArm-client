#!/usr/bin/env python
import socket
import cv2
import threading
import numpy
import pygame

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
color=False

def updsendpic(nothing, addr):
    while(True):
        ret, frame = cap.read()

        #import ipdb; ipdb.set_trace()

        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if not color:
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=numpy.rot90(frame)
        fr=frame.tostring()

        for i in xrange(20):
             udpsock.sendto(bytes(fr[i*46080:(i+1)*46080]), addr)


    cap.release()


def main():
    host = '127.0.0.1'
    port = 4004
    udp_port = 5005
    address = host, port
    udp_address = host, udp_port
    
    sock = socket.socket()
    #import ipdb; ipdb.set_trace()

    sock.bind(address)
    sock.listen(5)

    print("Server started...")

    while True:
        conn, addr = sock.accept()
        t = threading.Thread(target=updsendpic, args=('abc', udp_address))
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
        print("Client stopped!")


if __name__ == '__main__':
    main()
