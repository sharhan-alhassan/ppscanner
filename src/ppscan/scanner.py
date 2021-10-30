
import nmap

nmscan = nmap.PortScanner()

def scan_port(host, ports):
    print('     Host      Port   State')
    for port in (ports):
        nmscan.scan(host, port)
        port_state = nmscan[host]['tcp'][int(port)]['state']
        print('[*] ' + host + ' tcp/' + port + ' ' + port_state)


def scan_port_service_reason(host, ports):
    print('    Host      Port   State  Service  Reason')
    for port in ports:
        nmscan.scan(host, port)
        port_state = nmscan[host]['tcp'][int(port)]['state']
        port_service = nmscan[host]['tcp'][int(port)]['name']
        port_reason = nmscan[host]['tcp'][int(port)]['reason']
        print('[*] ' + host + ' tcp/' + port + ' ' + port_state + ' ' + port_service + ' ' + port_reason)


def scan_port_service(host, ports):
    print('     Host      Port   State   Service')
    for port in ports:
        nmscan.scan(host, port)
        port_state = nmscan[host]['tcp'][int(port)]['state']
        port_service = nmscan[host]['tcp'][int(port)]['name']
        print('[*] ' + host + ' tcp/' + port + ' ' + port_state + ' ' + port_service)


def scan_port_reason(host, ports):
    print('     Host      Port   State   Reason')
    for port in ports:
        nmscan.scan(host, port)
        port_state = nmscan[host]['tcp'][int(port)]['state']
        port_reason = nmscan[host]['tcp'][int(port)]['reason']
        print('[*] ' + host + ' tcp/' + port + ' ' + port_state + ' ' + port_reason)

