from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    Scan a TCP/IP host 
    """)
    parser.add_argument(
        "host",
        help='Hostname or IP to be scanned',
    )
    parser.add_argument(
        "port",
        help='Port number(s) of host separated by spaces',
        nargs='*'
    )
    parser.add_argument(
        '--service', '-s',
        help='Port service',
        metavar=("yes/no"),
        choices=['yes', 'no'],
    )
    parser.add_argument(
        '--reason', '-r',
        help='Port reason',
        metavar=("yes/no"),
        choices=['yes', 'no'],
    )
    return parser


def main():
    from ppscan import scanner

    args = create_parser().parse_args()
    if args.service and args.reason:
        print('Scanning...')
        scan = scanner.scan_port_service_reason(args.host, args.port)
        print('Scanning complete!')
        return scan

    elif args.service:
        print('Scanning...')
        scan = scanner.scan_port_service(args.host, args.port)
        print('Scanning complete!')
        return scan

    elif args.reason:
        print('Scanning...')
        scan = scanner.scan_port_reason(args.host, args.port)
        print('Scanning complete!')
        return scan

    else:
        print('Scanning...')
        scan = scanner.scan_port(args.host, args.port)
        print('Scanning complete!')
        return scan
