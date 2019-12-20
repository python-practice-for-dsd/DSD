import socket
from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer


def create_server(url='localhost', port=6789):
    server = SimpleXMLRPCServer((url, port))
    return server


def destroy_server(server):
    pass


def get_time_now_by_str():
    return str(datetime.now()).encode('utf-8')


def run_time_server():
    server = create_server()
    server.register_function(get_time_now_by_str, "test")
    server.serve_forever()
    return 'test'
