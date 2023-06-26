# IP-Calculator
IP-Calculator is a script designed to assist you with the topic of Subnetting

# Before executing the script, do the following:

`pip3 install colorama`

# Example:

```bash
❯ python3 ip_cal.py
usage: ip_cal.py [-h] --ip IP
ip_cal.py: error: the following arguments are required: --ip/-i
```

- This is the correct way

```bash
❯ python3 ip_cal.py -i 13.13.13.13/13
IP:  13.8.0.0
Netmask:  255.248.0.0
First IP:  13.8.0.0
Last IP:  13.15.255.255
Broadcast (Last IP):  13.15.255.255
Total de hosts:  524288
```
