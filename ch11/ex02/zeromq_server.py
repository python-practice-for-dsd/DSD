#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#


def create_server(url='127.0.0.1', port=6789):
    import zmq
    print("create server")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f'tcp://{url}:{port}')

    return socket


def get_time_now_by_bytes():
    import datetime
    return str(datetime.datetime.now()).encode('utf-8')

def run_time_server():
    socket = create_server()

    data = socket.recv()
    print(data.decode('utf-8'))
    if data.decode('utf-8') == 'test':
        now = get_time_now_by_bytes()
        socket.send(now)
    else:
        socket.send('end')

