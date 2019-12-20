#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

def connect_server(url='127.0.0.1', port=6789):
    import zmq

    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to hello world server…")
    socket = context.socket(zmq.REQ)
    socket.connect(f'tcp://{url}:{port}')

    socket.send(b"test")
    data = socket.recv()
    return data.decode('utf-8')