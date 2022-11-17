import asyncio
import aiohttp
import time
import url_handler
import os.path


async def fetch(session, q, print_func=print):
    while True:
        url = await q.get()
        try:
            async with session.get(url) as resp:
                data = await resp.read()
                top_k = url_handler.html_handler(data, k=1)
                print_func(f'url:{url}, top:{top_k}')
                assert resp.status == 200
        finally:
            q.task_done()


async def batch_fetch(urls, workers=5):
    q = asyncio.Queue()
    for url in urls:
        await q.put(url)

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch(session, q))
            for _ in range(workers)
        ]
        await q.join()

        for w in workers:
            w.cancel()


async def main(urls, num_workers=10):
    await batch_fetch(urls, workers=num_workers)


if __name__ == '__main__':
    with open(os.path.dirname(__file__) + '/../06/urls.txt') as f:
        URLS = [url[0:len(url) - 1] for url in f]
    counter = 0
    t1 = time.time()
    asyncio.run(main(URLS))
    t2 = time.time()
    print("time", t2 - t1)
    print("count", counter)
