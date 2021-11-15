from scapy.all import *
import sys

# const parameters for the program
TYPE = 1
ADDRESS = 2
WRONGTYPE = "wrong type\n"
IP_DST = "8.8.8.8"


def check_valid_ip(ip):
    """
    function check_valid_ip gets an ip address and checks if it a valid ip
    :param ip: the ip for check
    :return: True if the ip is valid and False if didn't
    """
    ip_list = ip.split(".")
    for octat in ip_list:
        if not octat.isdigit():
            return False
    return True


# a dictionary for types and managing them
TYPE_ADDRESS_DICTIONARY = {"PTR": check_valid_ip, "A": "www"}


def check_match_parameters(sys_type, address):
    """
    function check_match_parameters gets a type and an address and check if they fit
    :param sys_type: the type of the address
    :param address:the actual address
    :return: a tuple of validation and a comment if we need
    """
    chosen_type = sys_type.split("=")
    chosen_address = address.split(".")

    # case 1: the address don't good (there are type twice)
    if len(chosen_address) == 1:
        return False, "Can't find address for server {}: Non-existent domain".format(address)
    # case 2: there are 2 addresses
    elif len(chosen_type) == 1:
        return False, "the parameter {} isn't a type".format(sys_type)
    # case 3: switch between type and parameter
    elif len(chosen_address) == 1 and len(chosen_type) == 1:
        return False, "Can't find address for server {}: Non-existent domain".format(address)
    # case 4: the types aren't match to the address form
    elif (chosen_type[1] == "PTR" and not TYPE_ADDRESS_DICTIONARY[chosen_type[1]](address)) or (
            chosen_type[1] == "A" and TYPE_ADDRESS_DICTIONARY["PTR"](address)):
        return False, "the parameter: {} didn't match to the type: {}".format(address, chosen_type[1])
    # case 5: everything is good
    return True, []


def manage_type(sys_type):
    """
    function  manage_type gets a type and manage it
    :param sys_type: the type we manage by it
    :return: dns packet by the type or a warning if the type isn't good
    """
    if sys_type == 'type=A':
        dns_packet = IP(dst=IP_DST) / UDP(sport=24603, dport=53) / DNS(qdcount=1) / DNSQR(
            qname=sys.argv[ADDRESS])
    elif sys_type == 'type=PTR':
        ip_address = sys.argv[ADDRESS]
        reverse_ip = reverse_ip_for_revers_mapping(ip_address)
        dns_packet = IP(dst=IP_DST) / UDP(sport=24603, dport=53) / DNS(qdcount=1) / DNSQR(
            qname=reverse_ip + '.in-addr.arpa', qtype='PTR')
    else:
        dns_packet = WRONGTYPE
    return dns_packet


def reverse_ip_for_revers_mapping(ip):
    """
    function reverse_ip_for_revers_mapping gets an ip and reverse it (for reverse mapping)
    :param ip:the ip to reverse
    :return: a reveresed ip for example the ip 12.2.3.4 will reverse to 4.3.2.12
    """
    ip_list = ip.split(".")
    reverse_list = ip_list[::-1]
    return ".".join(reverse_list)


def print_list(some_list):
    """
    function print_list gets  a list and print it
    :param some_list: the list to print
    :return:
    """
    for obj in some_list:
        print(obj)
    return


def manage_sr1(dns_packet):
    """
    function manage_sr1 gets a dns packet and returns its rdata list from DNSRR
    :param dns_packet: the packet of dns
    :return: a list of al the rdata (ip and nested name if it exists)
    """
    r = sr1(dns_packet)
    count_list = [i for i in range(r[DNS].ancount)]
    rdata_list = []
    for i in count_list:
        rdata = r[DNSRR][i].rdata
        if isinstance(rdata, bytes):
            rdata_list += [rdata.decode()]
        else:
            rdata_list += [rdata]
    return rdata_list


def manage_less_parameters(parameters_list):
    """
    function manage_less_parameters checks if the user didn't enter parameters to type and/or address
    :param parameters_list: the list of the parameters the user enter
           (minimum 1 because he has to write the path of the file)
    """
    if len(parameters_list) == 2:  # the user enter only path and one of the parameters
        if parameters_list[1][:3] == "www":  # the 2nd parameter is a url address
            dns_packet = IP(dst=IP_DST) / UDP(sport=24603, dport=53) / DNS(qdcount=1) / DNSQR(
                qname=parameters_list[1])
            print_list(manage_sr1(dns_packet))
        elif check_valid_ip(parameters_list[1]):  # the 2nd parameter is an ip address
            reverse_ip = reverse_ip_for_revers_mapping(parameters_list[1])
            dns_packet = IP(dst=IP_DST) / UDP(sport=24603, dport=53) / DNS(qdcount=1) / DNSQR(
                qname=reverse_ip + '.in-addr.arpa', qtype='PTR')
            print_list(manage_sr1(dns_packet))
        else:  # the 2nd parameter is a type
            print("can't find {}: Non-existent domain\n".format(parameters_list[1]))

    elif len(parameters_list) == 1:  # the user enter only path
        print("you didn't send any parameters\n")
    return


def main():
    validation = False
    if len(sys.argv) == 3:  # the user enter 3 parameters
        validation, rdata_list = check_match_parameters(sys.argv[TYPE], sys.argv[ADDRESS])
        if validation:  # the parameters are in the right order
            dns_packet = manage_type(sys.argv[TYPE])
            if not dns_packet == WRONGTYPE:  # the type is good
                rdata_list = manage_sr1(dns_packet)
            else:  # the type is wrong
                rdata_list = [dns_packet]
            print_list(rdata_list)
        else:  # the parameter don't good (by order)
            print(rdata_list)
    else:  # the parameters don't good (by numbers)
        manage_less_parameters(sys.argv)


main()
