import asyncio
import aiohttp
import time
import url_handler
import os.path


async def fetch(session, q, print_func=print,
                handler_func=url_handler.html_handler):
    while True:
        url = await q.get()
        try:
            async with session.get(url) as resp:
                data = await resp.read()
                top_k = handler_func(data, k=1)
                print_func(f'url:{url}, top:{top_k}')
                assert resp.status == 200
        finally:
            q.task_done()


async def batch_fetch(urls_file, workers=5, print_func=print,
                      handler_func=url_handler.html_handler):
    q = asyncio.Queue()

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch(session, q, print_func, handler_func))
            for _ in range(workers)
        ]
        for url in urls_file:
            await q.put(url)
        await q.join()

        for w in workers:
            w.cancel()


async def main(urls_f, num_workers=10):
    await batch_fetch(urls_f, workers=num_workers)


if __name__ == '__main__':
    with open(os.path.dirname(__file__) + '/../06/urls.txt') as urls_f:
        counter = 0
        t1 = time.time()
        asyncio.run(main(urls_f))
        t2 = time.time()
        print("time", t2 - t1)
        print("count", counter)
