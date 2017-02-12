#!/usr/bin/python
import ListenerClass, os, signal


notConnected = True
started = False
listener = ListenerClass.listener()
os.system('cls' if os.name=='nt' else 'clear')
print "***************************************"
print "***************LISTENER****************"
print "***************************************"


while True:
    if notConnected and started:
        try:
            notConnected = False
            listener.start()
            notConnected = True
        except:
            notConnected = True
    console = raw_input()

    if console == "start":
        started = True
    elif console == "stop":
        started = False
	elif console == "status":
        if started:
			print "Listener running..."
		else:
			print "Listener not running..."
    elif console == "options":
        print "Set ipaddress:"
        ip = raw_input()
        print "set port:"
        port = int(raw_input())
        print "Listener configurated successfully."
        listener.setOptions(ip,port)
    elif console == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print "***************************************"
        print "***************LISTENER****************"
        print "***************************************"
    elif console == "exit":
        if notConnected or not started:
            os._exit(0)
    elif console == "^X":
        print "test"
    def sigint_handler(signum, frame):
        print 'Stop pressing the CTRL+C!'

    signal.signal(signal.SIGINT, sigint_handler)
