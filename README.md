## My Python Networking playground

Testing libraries, protocols and others (NETCONF, RESTCONF, gNMI, etc.)

The project includes some libraries I usually like:  

- [dynaconf](https://www.dynaconf.com/) for configuration management  
- [poetry](https://python-poetry.org/) dependency management  

Requests are performed using:  
- [aiohttp](https://docs.aiohttp.org/en/stable/index.html) for async HTTP / RESTCONF  
- [requests](https://requests.readthedocs.io/en/latest/) for sync HTTP / RESTCONF 
- [ncclient](https://github.com/ncclient/ncclient) for NETCONF  


_Note: Connect to a Cisco sandbox via SSH may require ssh options_  

`ssh -oKexAlgorithms=+diffie-hellman-group14-sha1  developer@sandbox-iosxe-recomm-1.cisco.com`  

depending on the protocol version they offer.  

### TODO
- implement grpc calls for gNMI
- implement minimal REACT dashboard to show info / invoke command


