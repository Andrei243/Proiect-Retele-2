# inainte de toate trebuie adaugata o regula de ignorare 
# a pachetelor RST pe care ni le livreaza kernelul automat
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
from scapy.all import *

ip = IP()
ip.src ="172.11.0.14" # ip-ul nostru
ip.dst ="198.12.0.14" # ip-ul serverului
ip.show()

tcp = TCP()
tcp.sport =5000 # un port la aleger
tcp.dport =5000 # portul destinatie pe care ruleaza serverul
tcp.seq =50 # un sequence number la alegere
tcp.flags = 'S'
tcp.options=[('MSS',2)]
tcp.show()


SYN = ip/tcp
SYN.show()
raspuns_SYN_ACK = sr1(SYN)
rasp_ack = raspuns_SYN_ACK.seq + 1
rasp_seq = tcp.seq + 1
print("Heya")
tcp.seq = rasp_seq
tcp.ack = rasp_ack
tcp.flags = 'A'

ACK= ip / tcp
raspuns_ACK = sr1(ACK)
data=[]
data.append('a')
data.append('b')
data.append('c')
data.append('def')
for dat in data:
    tcp.seq = tcp.seq + 1
    tcp.ack = raspuns_ACK.seq + 1
    mesaj = ip / tcp / dat
    raspuns_ACK = sr1(mesaj)
    raspuns_ACK.show()


tcp.seq=tcp.seq+1
tcp.ack=raspuns_ACK.seq+1
tcp.flags='FIN'

FIN=ip/tcp
raspuns_FIN=sr1(FIN)




