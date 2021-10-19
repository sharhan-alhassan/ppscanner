
import click

from app import application

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-h', '--host', type=str, help="Hostname to be scanned")
@click.option('-p', '--port', type=str, help="Port number(s) to be scanned")
@click.option('-s', '--name', is_flag=True, help="Add this flag to see the service running in this port")
@click.option('-r', '--reason', is_flag=True, help="Add this flag to see the tcp handshake type.")
def scan(host, port, name, reason):
    ports = str(port).strip("'").split(',')
    click.echo('Scanning for ports...')
    for port in ports:
        start_scan = application.scan_port(host, port, name, reason)
        return start_scan