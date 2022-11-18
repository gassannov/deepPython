import asyncio
import io
from async_url_process import fetch, batch_fetch
from unittest import mock
from unittest import IsolatedAsyncioTestCase


class AsyncTest(IsolatedAsyncioTestCase):
    async def test_fetch(self):
        url = 'https://en.wikipedia.org/wiki/Christian_Weise'
        top = 'foo'

        handler_mock = mock.Mock()
        session_mock = mock.Mock()
        resp_mock = mock.AsyncMock()

        handler_mock.return_value = top
        print_mock = mock.Mock()

        q = asyncio.Queue()
        await q.put(url)

        get_mock = mock.MagicMock()
        get_mock.__aenter__.return_value = resp_mock
        session_mock.get.return_value = get_mock

        read_mock = mock.AsyncMock()
        read_mock.return_value = url
        resp_mock.read = read_mock
        resp_mock.status = 200

        tsk = asyncio.create_task(fetch(session_mock, q, print_mock, handler_mock))
        await q.join()
        tsk.cancel()

        print_mock.assert_called_once_with(f'url:{url}, top:{top}')
        self.assertEqual(print_mock.call_count, 1)

    async def test_batch_fetch(self):
        urls = ['https://en.wikipedia.org/wiki/Christian_Weise']*10
        top = 'foo'
        resp = io.StringIO()
        def print_mock(data): print(data, file=resp)

        handler_mock = mock.Mock()
        handler_mock.return_value = top
        await batch_fetch(urls, handler_func=handler_mock, print_func=print_mock)
        self.assertEqual(handler_mock.call_count, 10)
        self.assertTrue(resp.getvalue() == f'url:{urls[0]}, top:{top}\n'*10)
