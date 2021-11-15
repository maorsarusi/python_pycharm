from scapy.all import *


def main():
    syn_segment = TCP(dport=80, seq=123, flags='S')
    syn_packet = IP(dst='www.google.com') / syn_segment
    syn_ack_packet = sr1(syn_packet, verbose=0)
    ack_segment = TCP(sport=syn_ack_packet.dport, dport=80, seq=syn_ack_packet.ack, flags='A')
    ack_packet = IP(dst='www.google.com') / ack_segment
    send(ack_packet)
    ack_packet.show()


if __name__ == "__main__":
    main()
