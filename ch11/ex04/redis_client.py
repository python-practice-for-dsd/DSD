from time import sleep
import ch11.redis_server as s

def connect_server():
    r = s.create_server()
    timeout = 10
    ret = []
    key = 'chocolate'
    for i in range(10):
        sleep(0.5)
        msg = r.blpop(key, timeout)
        remaining = r.llen(key)
        if msg:
            value = msg[1]
            ret.append(value)
            print('Lucy got a', value, 'only', remaining, 'left')
    return ret
