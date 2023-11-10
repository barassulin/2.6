import socket
MAX_PACKET = 1024
IP = "127.0.0.1"
PORT = 1729


def main():
    my_socket = socket.socket()
    try:
        my_socket.connect((IP, PORT))
        my_socket.send(bytes(4))
        msg = input("pls enter a message: ")
        my_socket.send(msg.encode())
        response = my_socket.recv(MAX_PACKET).decode()
        while response != "EXIT":
            print("server responded with: " + (response))
            msg = input("pls enter a message: ")
            my_socket.send(msg.encode())
            response = my_socket.recv(MAX_PACKET).decode()
    except socket.error as error:
        print("socket error:" + str(error))

    finally:
        my_socket.close()


if __name__ == "__main__":
    main()