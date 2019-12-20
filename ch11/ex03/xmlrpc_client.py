import xmlrpc.client


def connect_server():
    proxy = xmlrpc.client.ServerProxy("http://localhost:6789")
    bin :xmlrpc.client.Binary = proxy.test()
    ret : str = bin.data.decode('utf-8')
    return ret
