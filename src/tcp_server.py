# TCP Server
import socket
import logging
import time
# from scapy.all import *

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5000
adresa = 'localhost'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
sock.listen(5)
logging.info('Asteptam conexiui...')
conexiune, address = sock.accept()
logging.info("Handshake cu %s", address)
while True:

    data = conexiune.recv(1)
    logging.info('Content primit: "%s"', data)
    conexiune.send("Q")
conexiune.close()
sock.close()
