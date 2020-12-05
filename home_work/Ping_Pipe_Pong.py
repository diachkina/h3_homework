from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(receiver, sender, response):
    while True:
        receiver.recv()
        print(f"Process{getpid()} got message: {response}")
        sleep(2)
        sender.send(response)


if __name__ == "__main__":
    receiver1, sender1, = Pipe()
    receiver2, sender2, = Pipe()
    process_1 = Process(target=ponger, args=(receiver1, sender2, 'Ping')).start()
    process_2 = Process(target=ponger, args=(receiver2, sender1, 'Pong')).start()
    sender1.send("Let's play!")
