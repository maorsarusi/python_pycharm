from scapy.all import *
from time import *


def main():
    i = 1
    j = 0
    while True:
        t1 = time()
        tracert_packet = IP(ttl=i, dst="www.google.com") / ICMP()
        res = sr1(tracert_packet, verbose=0, timeout=5)
        t2 = time()
        try:
            print("ip address: {}, {} ms".format(res[IP].src, (t2 - t1) * 100))
            j += 1
            if res[ICMP].type == 0:
                break

        except TypeError:
            print("REQUST TIME OUT")
        i += 1
    print("number of routers: {}".format(j))


if __name__ == "__main__":
    main()
