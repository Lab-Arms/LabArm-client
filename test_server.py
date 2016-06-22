#!/usr/bin/env python
import socket
import cv2
import threading


def updsendpic(nothing, addr):
    cap = cv2.VideoCapture(0)
    udphost = addr[0]
    udpport = addr[1] + 1
    udpserver = (udphost, udpport)
    udpclient = (udphost, udpport + 1)
    import ipdb; ipdb.set_trace()
    
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsock.bind(udpserver)
    connected = True
    udpsock.sendto('conectado', udpclient)
    data, addr = udpsock.recvfrom(1024)
    if data == 'eh nois':
        pass
    while connected:
        ret, frame = cap.read()
        all_bytes = frame.tobytes()
        to_send = all_bytes[:987]
        all_bytes = all_bytes[987:]
        while all_bytes != '':
            udpsock.sendto(to_send, udpclient)
            to_send = all_bytes[:987]
            all_bytes = all_bytes[987:]

    cap.release()


def main():
    host = '127.0.0.1'
    port = 4004
    address = host, port
    
    sock = socket.socket()
    #import ipdb; ipdb.set_trace()

    sock.bind(address)
    sock.listen(5)

    print("Server started...")

    while True:
        conn, addr = sock.accept()
        t = threading.Thread(target=updsendpic, args=('abc', address))
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
