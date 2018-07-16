import threading
from threading import Event
import socket, select

timeSendFPacket = 0
totalDelayAllP = 0


class WiFi_Listener(threading.Thread):
    def __init__(self, IP_Port):
        threading.Thread.__init__(self)
        self.BUFF = 1024
        self.HOST = ''  # must be input parameter
        self.PORT = IP_Port  # must be input parameter
        self.WiFi_Init()
        self.Data = None
        self.clientsock = None
        self.IP_Address = None
        self.counter = 0
        self.stop_threads = Event()

    def WiFi_Init(self):
        print "--------------------------------------------"
        print "[C_WiFi_Server] WiFi_Init Initilazing Server ... ... ... ...  !!!"
        self.ADDR = (self.HOST, self.PORT)
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversock.bind(self.ADDR)

    def run(self):
        self.WiFi_Packet_Receive()

    def stop(self):
        self.stop_threads.set()

    def WiFi_Packet_Receive(self):
        self.serversock.listen(300)
        print "[C_WiFi_Server] WiFi_Packet_Receive Listening on port", self.PORT
        print "--------------------------------------------"
        read_list = [self.serversock]
        while not self.stop_threads.is_set():
            readable, writable, errored = select.select(read_list, [], [], 10)

            for rlist in readable:
                if rlist is self.serversock:
                    self.clientsock, addr = self.serversock.accept()
                    read_list.append(self.clientsock)
                else:
                    data_R = rlist.recv(1000)
                    if not data_R:
                        read_list.remove(rlist)
                        continue
                    self.Data = data_R

                    # Processing data start here
                    print "[C_WiFi_Server] WiFi_Packet_Receive data received: ", data_R
                    # Processing data end here

if __name__ == '__main__':
    S_TS = WiFi_Listener(5000)
    S_TS.start()
