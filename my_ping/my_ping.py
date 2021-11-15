from scapy.all import *
import sys

SYS_IP = 1
NUM_OF_PACKETS = 2


def my_ping(ip, num_of_packets):
    req = IP(dst=ip) / ICMP(type="echo-request")

    for i in range(int(num_of_packets)):
        r = req / "number of package: {}".format(str(i + 1))
        _ = sr1(r, verbose=0)

    print("Sending {} packets to {}".format(num_of_packets, ip))
    print("Received {} reply packets")
    return


def main():
    send_ip = sys.argv[SYS_IP]
    num_of_packets = sys.argv[NUM_OF_PACKETS]
    my_ping(send_ip, num_of_packets)


if __name__ == "__main__":
    main()
