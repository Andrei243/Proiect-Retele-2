from scapy.all import *

eth=Ether(dst="ff:ff:ff:ff:ff:ff")


def catre_20(string):
    while len(string)<20:
        string=string+" "
    return string


tabel=""

offset=16
adresa="198.13.0.14"+"/"+str(offset)

answered,unanswered = srp(eth/ARP(pdst=adresa),timeout=20)
print ("IP                  MAC")

for send,rec in answered:
    mac=rec.sprintf("%Ether.src%")
    ip=rec.sprintf("%ARP.psrc%")
    tabel+=catre_20(ip)+mac+"\n"
print(tabel)