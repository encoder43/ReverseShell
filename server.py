import socket
import sys


# creating the socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error :" + str(msg))


# binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port : " + str(port))

        s.bind((host, port))
        s.listen(s)

    except socket.error as msg:
        print(" socket bind error" + str(msg) + "\n" + "retrying....")
        bind_socket()


# establish connection with a client socket must be listening

def socket_accept():
    conn, address = s.accept()
    print("connection is established" + "IP" + address[0] + "Port" + str(address[1]))
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()
