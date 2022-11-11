import socket
import sys
import time
# from threading import Thread
import threading
import queue


def print_data(data, thread_id):
    print(data.decode() + f' thread:{thread_id}')


def make_socket_func() -> socket:
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Client:
    def __init__(self, urls, thread_count=10,
                 data_handler=print_data, make_socket=make_socket_func):
        self.urls = urls
        self.thread_count = thread_count
        self.url_queue = queue.Queue()
        self.threads = [
            threading.Thread(target=self.send_urls, args=[i], daemon=True)
            for i in range(self.thread_count)]
        self.data_handler = data_handler
        self.make_socket = make_socket
        for thread in self.threads:
            thread.start()

    def put_data(self):
        for url in self.urls:
            self.url_queue.put(url)
        for thread in self.threads:
            thread.join()

    def send_urls(self, thread_id=None):
        while True:
            url = self.url_queue.get()
            if url == 'end':
                self.url_queue.put('end')
                break
            client_sock = self.make_socket()
            client_sock.connect(('127.0.0.1', 53210))
            client_sock.sendall(url.encode())
            data = client_sock.recv(1024)
            self.data_handler(data, thread_id)
            client_sock.close()


if __name__ == '__main__':
    with open(sys.argv[2], "r") as file_:
        urls = [url[0:len(url)-1] for url in file_]
    urls.append('end')
    client = Client(urls=urls, thread_count=int(sys.argv[1]))
    start = time.time()
    client.put_data()
    end = time.time()
    print(f'Time passed for {sys.argv[1]} threads: {end-start}')
