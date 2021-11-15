from scapy.all import *

p1 = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst='8.8.8.8')/Raw("abc")
sendp(p1)
print('***')
p2 = Ether()/IP(dst='8.8.8.8')/Raw("def")
sendp(p2)
print('***')
p3 = IP(dst='8.8.8.8')/Raw("ghi")
send(p3)
print('***')
p4 = IP(dst='8.8.8.8')/Raw("jkl")
send(p4)
