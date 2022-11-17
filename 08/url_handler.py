from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


# class AsyncURLHandler:
#     def __init__(self, url, top_k=5):
#         self.url = url
#         self.top_k = top_k
#
#     async def __aenter__(self):
#         url_responce = await url_handler(self.url, self.top_k)
#         return url_responce
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         pass


def html_handler(html, k):
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text_set = text.split()
    counter = Counter(text_set)
    most_occur = dict(counter.most_common(k))
    return most_occur
