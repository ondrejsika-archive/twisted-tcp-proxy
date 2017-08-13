from __future__ import print_function
import argparse
from twisted.internet import reactor, protocol


class ClientProtocol(protocol.Protocol):
    def dataReceived(self, data):
        print("server", data)
        server_protocol.transport.write(data)

    def connectionLost(self, reason):
        server_protocol.transport.loseConnection()
        reactor.stop()


class ClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return client_protocol


class ServerProtocol(protocol.Protocol):
    def dataReceived(self, data):
        print("client", data)
        client_protocol.transport.write(data)

    def connectionLost(self, reason):
        client_protocol.transport.loseConnection()


class ServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return server_protocol


client_protocol = ClientProtocol()
server_protocol = ServerProtocol()


parser = argparse.ArgumentParser()
parser.add_argument('listen_port', type=int)
parser.add_argument('connect_host')
parser.add_argument('connect_port', type=int)

args = parser.parse_args()

reactor.listenTCP(args.listen_port, ServerFactory())
reactor.connectTCP(args.connect_host, args.connect_port, ClientFactory())
reactor.run()


