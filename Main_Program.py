import C_WiFi_Server as Server
import time

S_TS = Server.WiFi_Listener(5000)
S_TS.start()

time.sleep(2)
while 1:
    # Do something here
    print "Do something here..."
    time.sleep(1)
