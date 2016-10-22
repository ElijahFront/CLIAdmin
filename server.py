import socket
import sys

# Create socket that allows two comps to connect


def socket_create():
    try:
        global host
        global port
        global sock
        host = ''
        port = 9999
        sock = socket.socket()
    except socket.error as msg:
        print("Socket error" + str(msg))

# Bind socket to the port and wait for connection

print(socket.gethostbyname(socket.gethostname()))


def socket_bind():
    try:
        global host
        global port
        global sock
        print("Binding socket to the port " + str(port))
        sock.bind((host, port))
        sock.listen(5)

    except socket.error as msg:
        print("Socket binding error" + str(msg) + '\n' + 'Retrying...')
        socket_bind()

# Establish connection


def socket_accept():
    conn, address = sock.accept()
    print('Connection has been established \n IP: ' + address[0]
          + '\nPort: ' + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            sock.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), encoding='utf-8')
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
