# inainte de toate trebuie adaugata o regula de ignorare 
# a pachetelor RST pe care ni le livreaza kernelul automat
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
from scapy.all import *
import struct

optiune = 'MSS'
op_index = TCPOptions[1][optiune]
op_format = TCPOptions[0][op_index]
valoare = struct.pack(op_format[1], 2)

ip = IP()
ip.src ="172.111.0.14" # ip-ul nostru
ip.dst ="198.13.0.14" # ip-ul serverului


tcp = TCP()
tcp.sport =5000 # un port la aleger
tcp.dport =10000 # portul destinatie pe care ruleaza serverul
tcp.seq =50 # un sequence number la alegere
tcp.flags = 'S'
tcp.option = [(optiune, valoare)]

# tcp.show()


SYN = ip/tcp
SYN.show()
raspuns_SYN_ACK = sr1(SYN)
rasp_ack = raspuns_SYN_ACK.seq + 1
rasp_seq = tcp.seq + 1
tcp.seq = rasp_seq
tcp.ack = rasp_ack
tcp.flags = 'A'

ACK= ip / tcp
send(ACK)
data=[]
data.append('a')
data.append('b')
data.append('c')
data.append('def')
for dat in data:
    tcp.seq = tcp.seq + 1
    tcp.ack = tcp.seq + 1
    tcp.flags="PA"
    mesaj = ip / tcp / dat
    mesaj.show()
    raspuns_ACK = sr1(mesaj)

tcp.seq=tcp.seq+1
tcp.ack=raspuns_ACK.seq+1
tcp.flags='FA'

FIN=ip/tcp
raspuns_FIN=sr1(FIN)

tcp.seq=tcp.seq+1
tcp.ack=raspuns_FIN.seq+1
tcp.flags='A'
FINACK=ip/tcp
send(FINACK)




