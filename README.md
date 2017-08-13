# Twisted TCP Proxy

    Ondrej Sika <ondrej@ondrejsika.com>

Simple TCP proxy prints communication between server and client. Build for testing Stratum protocol.

## Install

```
virtualenv .env
. .env/bin/activate
pip install -r requirements.txt
```

## Run

```
. .env/bin/activate
python proxy.py <listen_port> <connect_host> <connect_port>
```


