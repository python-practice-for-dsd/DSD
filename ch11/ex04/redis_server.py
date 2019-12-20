import redis
import random
from time import sleep
def create_server():
    myHostname = ""
    myPassword = ""
    print("create start")
    r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword, ssl=True)
    print("create end")
    return r


def run_time_server():
    r = create_server()
    values = ['godiva', 'meiji', 'morinaga']
    key = 'chocolate'
    for i in range(10):
        seconds = random.random()
        sleep(seconds)
        value = random.choice(values)
        r.rpush(key, value)

def ping(r):
    result = r.ping()
    print("Ping returned : " + str(result))
