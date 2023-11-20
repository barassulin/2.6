"""
Author: Bar Assulin
Date: 19.11.2023
Description: server.py for cyber2.6
"""

import socket
import os
import logging

MAX_PACKET = 1024
IP = "127.0.0.1"
PORT = 1729
LOG_FORMAT = '%(levelname)s | %(asctime)s | %(processName)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/client.log'


def main():
    """
    main
    return: the response to your request
    """
    my_socket = socket.socket()
    try:
        my_socket.connect((IP, PORT))
        msg = input("pls enter a message: ")
        logging.debug("sending msg request" + msg)
        my_socket.send(msg.encode())
        response = my_socket.recv(MAX_PACKET).decode()
        logging.debug("getting response" + response)
        while response != "EXIT":
            print("server responded with: " + response)
            msg = input("pls enter a message: ")
            my_socket.send(msg.encode())
            response = my_socket.recv(MAX_PACKET).decode()
    except socket.error as error:
        logging.error("received socket error" + str(error))
        print("socket error:" + str(error))

    finally:
        my_socket.close()


if __name__ == "__main__":
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()
