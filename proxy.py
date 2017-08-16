from __future__ import print_function
import argparse
from twisted.internet import reactor, protocol


class ClientProtocol(protocol.Protocol):
    def __init__(self, conn_id):
        self.conn_id = conn_id

    def dataReceived(self, data):
        print("server %s" % self.conn_id, data)
        self.server_protocol.transport.write(data)

    def connectionLost(self, reason):
        self.server_protocol.transport.loseConnection()


class ClientFactory(protocol.ClientFactory):
    def __init__(self, server_protocol):
        self.server_protocol = server_protocol

    def buildProtocol(self, addr):
        client_protocol = ClientProtocol(self.server_protocol.conn_id)
        client_protocol.server_protocol = self.server_protocol
        self.server_protocol.client_protocol = client_protocol
        return client_protocol


class ServerProtocol(protocol.Protocol):
    def __init__(self, conn_id):
        self.conn_id = conn_id

    def dataReceived(self, data):
        print("client %d" % self.conn_id, data)
        self.client_protocol.transport.write(data)

    def connectionLost(self, reason):
        self.client_protocol.transport.loseConnection()


class ServerFactory(protocol.Factory):
    def __init__(self):
        self.conn_counter = 0

    def buildProtocol(self, addr):
        conn_id = self.conn_counter
        self.conn_counter += 1
        server_protocol = ServerProtocol(conn_id)
        reactor.connectTCP(args.connect_host, args.connect_port, ClientFactory(server_protocol))
        return server_protocol


parser = argparse.ArgumentParser()
parser.add_argument('listen_port', type=int)
parser.add_argument('connect_host')
parser.add_argument('connect_port', type=int)

args = parser.parse_args()

reactor.listenTCP(args.listen_port, ServerFactory())
reactor.run()


