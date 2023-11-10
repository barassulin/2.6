import socket
import datetime
import random

QUEUE_LEN = 1
MAX_PACKET = 1024


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        my_socket.bind(('0.0.0.0', 1729))
        my_socket.listen(QUEUE_LEN)
        while (True):
            client_socket, client_address = my_socket.accept()
            try:
                request = client_socket.recv(MAX_PACKET).decode()
                while request != "EXIT":
                    if request == "TIME":
                        date = str(datetime.datetime.now())
                        client_socket.send(date.encode())
                    elif request == "NAME":
                        name = "server_hypothalamus"
                        client_socket.send(name.encode())
                    elif request == "RAND":
                        number = random.randint(1, 10)
                        number = str(number)
                        client_socket.send(number.encode())
                    request = client_socket.recv(MAX_PACKET).decode()

            except socket.error as err:
                print('received socket error on client socket' + str(err))

            finally:
                msg = "EXIT"
                client_socket.send(msg.encode())
                client_socket.close()
    except socket.error as err:
        print('received socket error on server socket' + str(err))

    finally:
        my_socket.close()


if __name__ == "__main__":
    main()