# Portable Port Scanner (ppscanner)
Portable Port Scanner (ppscanner) is a light-weight open-source CLI utility that leverages on `nmap` to make quick and elegant scanning of host devices and their ports for better insights, troubleshooting, check vulnerabilites and meet compliance requirements of networks.

## Installation Guide 

### Global dependencies
- ppscanner leverages on `nmap` functionalities so you need it installed to be able use it.

```bash
$ sudo apt-get install nmap
```

### Project Dependencies
```bash
$ pip install -i https://test.pypi.org/simple/ ppscanner

```

### Run Commands
- Example code for IP Address: 127.0.0.1 and Port: 80
- It automatically gives the port(tcp) and state(open/closed)
```bash
$ ppscan scan 127.0.0.1 80
```

### Optional arguments
- Other optional arguments are `--service` with input of `yes or no` and `reason` with input `yes or no`


### Help commands
```bash
$ ppscan scan --help
```
