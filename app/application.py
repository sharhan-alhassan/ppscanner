

import nmap
import click


'''
Automatic: Port and state
Optional: Name and reason
nmscan[host].all_protocols() //['tcp, udp']
nmscan[host]['tcp'].keys() // [21,22,80]
'''
nmscan = nmap.PortScanner()

def render_state(host, port):
    nmscan.scan(host, port)
    port_state = nmscan[host]['tcp'][int(port)]['state']
    return port_state


def render_name(host, port):
    nmscan.scan(host, port)
    port_name = nmscan[host]['tcp'][int(port)]['name']
    return port_name


def render_reason(host, port):
    nmscan.scan(host, port)
    port_reason = nmscan[host]['tcp'][int(port)]['reason']
    return port_reason


def scan_port(host, port, name, reason):
    if name and reason:
        port_state = render_state(host, port)
        port_name = render_name(host, port)
        port_reason = render_reason(host, port)
        click.echo('[*] ' + host + ' tcp/' + port + ' ' + port_state + ' ' + port_name + ' ' + port_reason)
    elif name or reason:
        if name:
            port_state = render_state(host, port)
            port_name = render_name(host, port)
            click.echo('[*] ' + host + ' tcp/' + port + ' ' + port_state + ' ' + port_name)
        else:
            port_state = render_state(host, port)
            port_reason = render_reason(host, port)
            click.echo('[*] ' + host + ' tcp/' + port + ' ' + port_state + ' ' + port_reason)
    else:
        port_state = render_state(host, port)
        click.echo('[*] ' + host + ' tcp/' + port + ' ' + port_state)

