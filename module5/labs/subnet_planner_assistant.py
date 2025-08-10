# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# subnet planner script, takes a ip-address and subnet-mask from the user and -
# outputs network address, broadcast address, number of usable hosts and -
# first/last usable IPs in the range

import ipaddress

def subnet_calculator(ip, mask):
    """
    calculates netaddr, broadcast addr, usable hosts, and first&last usable IP-addr

    args: str: ip = ip address,
          str: mask = subnet mask (e.g.,24 or , 255.255.255.0)

    returns: dict: {
        "Network Address": str(network_address),
        "Broadcast Address": str(broadcast_address),
        "Usable Hosts": usable_hosts,
        "IP Range": ip_range (list of str)
    }
    """

    network = ipaddress.ip_network(f'{ip}/{mask}', strict=False)

    # defining our variable values
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    usable_hosts = network.num_addresses - 2

    # creates a list of all usable host IP addresses in the subnet as strings
    ip_range = [str(ip) for ip in network.hosts()]

    return {
        "Network Address": str(network_address),
        "Broadcast Address": str(broadcast_address),
        "Usable Hosts": usable_hosts,
        "IP Range": ip_range
    }

def main():
    """
    Main Driver program
    """

    try:
        # prompt user for data
        ip_input = input('Enter IP-Address: ')
        subnet_mask = input('Enter Subnet Mask: ')

        # call subnet_calculator() and save whats returned to subnet_info
        subnet_info = subnet_calculator(ip_input, subnet_mask)

        print("\nNetwork Address:", subnet_info["Network Address"])
        print("Broadcast Address:", subnet_info["Broadcast Address"])
        print("Number of Usable Hosts:", subnet_info["Usable Hosts"])
        print("IP Range from", subnet_info["IP Range"][0], "to", subnet_info["IP Range"][-1])
    except ValueError:
        print('Please enter a valid format for IP and Mask.')

if __name__ == "__main__":
    main()