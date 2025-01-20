# ddclient-fritz

This repository contains a docker image and configuration to run ddclient.
[fritzconnection](https://github.com/kbr/fritzconnection) is used to query
a FritzBox for its current WAN-ipv6.

## Usage

1. Create the image and docker volumes: `docker compose create`
2. Add your DynDNS to the protocol section of ddclient.conf.
3. Copy configuration files into the volumes (and set correct file permissions!):
```
cp ddclient.conf <docker volume path>/ddclient-fritz_config
cp cmd/cmd-getwanipv6-fritzbox.py cmd/cmd-getwanipv6-fritzbox.sh <docker volume path>/ddclient-fritz_cmd
```
4. Add your FritzBox credentials and address to the env file `fritzconnection.env`.
5. Start stack: `docker compose up`
