from time import sleep
import string

def create_server(url='127.0.0.1', port=6789):
    import zmq
    print("create server")
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f'tcp://{url}:{port}')

    return socket


def get_time_now_by_bytes():
    import datetime
    return str(datetime.datetime.now()).encode('utf-8')

def read_text(filename:str) -> str:
    with open(filename, 'rt') as poem:
        return poem.read()

def run_time_server():

    pub = create_server()

    sleep(1)

    words = read_text('mammoth.txt')
    print(words.split())
    for word in words.split():
        word = word.strip(string.punctuation)
        data = word.encode('utf-8')
        if word.startswith(('a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O')):
            print('vowels', data)
            pub.send_multipart([b'vowels', data])
        if len(word) == 5:
            print('five', data)
            pub.send_multipart([b'five', data])

