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
    sub = context.socket(zmq.SUB)
    sub.connect(f'tcp://{url}:{port}')
    sub.setsockopt(zmq.SUBSCRIBE, b'vowels')
    sub.setsockopt(zmq.SUBSCRIBE, b'five')
    while True:
        topic, word = sub.recv_multipart()
        print(topic, word)
