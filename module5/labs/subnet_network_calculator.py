# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# subnetting calculator script that outputs host bits, total ips, and total usable ips

def subnet_host_bit_calculator(prefix):
    """
    calculates host bits, total IPs, and total usable IPs

    args: int: prefix = subnet mask as CIDR notation (e.g., 24, 25 ,26, etc)

    prints:
        f"Subnet: /{prefix_length}"
        f"Host Bits: {host_bits}"
        f"Total Addresses: {total_hosts}"
        f"Usable Hosts: {usable_hosts}"
    """

    if not (0 <= prefix <= 32):
        print('Invalid prefix length. must be between 0 and 32')
        return
    
    # assign values to variables
    host_bits = 32 - prefix
    total_hosts = 2 ** host_bits
    usable_hosts = total_hosts - 2 if host_bits > 1 else 0

    print(f"\nSubnet: /{prefix}")
    print(f"Host Bits: {host_bits}")
    print(f"Total Addresses: {total_hosts}")
    print(f"Usable Hosts: {usable_hosts}")

def main():
    """
    Main Driver program
    """
    
    print('--- Subnet Host Bit Calculator ---')
    try:
        user_input = int(input('Enter subnet prefix(e.g., 24 for /24): '))
        subnet_host_bit_calculator(user_input)
    except ValueError:
        print('Please enter valid integer')

if __name__ == "__main__":
    main()