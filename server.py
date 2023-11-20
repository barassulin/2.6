"""
Author: Bar Assulin
Date: 19.11.2023
Description: server.py for cyber2.6
"""

import socket
import datetime
import random
import os
import logging

QUEUE_LEN = 1
MAX_PACKET = 1024
NAME = "server_stars"
LOG_FORMAT = '%(levelname)s | %(asctime)s | %(processName)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/server.log'


def time_request():
    """
    returns time right now
    returns: time
    """
    date = str(datetime.datetime.now())
    return date


def name_request():
    """
    returns server name
    returns: name
    """
    return NAME


def random_request():
    """
    returns int number
    returns: random number
    """
    number = random.randint(1, 10)
    number = str(number)
    return number


def main():
    """
    main
    return: response to a request from a client
    """
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        my_socket.bind(('0.0.0.0', 1729))
        my_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = my_socket.accept()
            try:
                request = client_socket.recv(MAX_PACKET).decode()
                logging.debug("getting request" + request)
                while request != "EXIT":
                    if request == "TIME":
                        comment = time_request()
                    elif request == "NAME":
                        comment = name_request()
                    elif request == "RAND":
                        comment = random_request()
                    else:
                        comment = "enter one request from the options: NAME/TIME/RAND/EXIT"

                    logging.debug("sending comment" + comment)

                    client_socket.send(comment.encode())
                    request = client_socket.recv(MAX_PACKET).decode()
                    logging.debug("getting request" + request)

            except socket.error as err:
                logging.error("received socket error on client socket" + str(err))
                print('received socket error on client socket' + str(err))

            finally:
                msg = "EXIT"
                client_socket.send(msg.encode())
                client_socket.close()
    except socket.error as err:
        logging.error("received socket error on server socket" + str(err))
        print('received socket error on server socket' + str(err))

    finally:
        my_socket.close()


if __name__ == "__main__":
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    assert name_request() == NAME
    assert 10 > int(random_request()) > 0
    assert time_request() == str(datetime.datetime.now())
    main()
