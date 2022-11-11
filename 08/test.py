import asyncio
import aiohttp
import time


URL = "https://docs.python.org/3/whatsnew/3.11.html"
URLS = [URL] * 50
counter = 0


async def fetch(session, q):
    while True:
        url = await q.get()
        print(q.qsize())
        global counter
        counter += 1

        try:
            async with session.get(url) as resp:
                data = await resp.read()
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


async def main():
    await batch_fetch(URLS, workers=1)


t1 = time.time()

asyncio.run(main())

t2 = time.time()
print("time", t2 - t1)
print("count", counter)
