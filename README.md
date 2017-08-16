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

## Docker

Add support for Docker

### Build

```
docker build . -t twisted-tcp-proxy
```

### Run

```
docker run -p <listen_port>:<listen_port> twisted-tcp-proxy <listen_port> <connect_host> <connect_port>
```

Example:

```
docker run -p 3333:3333 twisted-tcp-proxy 3333 stratum.slushpool.com 3333
```

### Run from external source code

```
docker run -p <listen_port>:<listen_port> -v `pwd`/proxy.py:/app/proxy.py twisted-tcp-proxy <listen_port> <connect_host> <connect_port>
```

Example:

```
docker run -p 3333:3333 -v `pwd`/proxy.py:/app/proxy.py twisted-tcp-proxy 3333 stratum.slushpool.com 3333
```
