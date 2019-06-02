from scapy.all import *

eth=Ether(dst="ff:ff:ff:ff:ff:ff")


def catre_20(string):
    while len(string)<20:
        string=string+" "
    return string


tabel=""

# for i in range(0,256):
#     for j in range(0,256):
#         dest="198.12."+str(i)+"."+str(j)
#         arp=ARP(pdst=dest)
#         answered, unanswered=sr(eth/arp,retry=0,timeout=1)
#         if len(answered)>0:
#             tabel+=catre_20(answered[1].psrc)+answered[1].hwsrc+"\n"
# print(tabel)

offset=16
adresa="198.13.0.14"+"/"+str(offset)

answered,unanswered = srp(eth/ARP(pdst=adresa),timeout=20)
print ("IP                  MAC")

for send,rec in answered:
    mac=rec.sprintf("%Ether.src%")
    ip=rec.sprintf("%ARP.psrc%")
    tabel+=catre_20(ip)+mac+"\n"
    # print("ans")
    # print(rec.sprintf(r"%ARP.psrc% -- %Ether.src%"))
print(tabel)