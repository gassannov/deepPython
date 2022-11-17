import asyncio
import unittest
from main import fetch, batch_fetch
from unittest import mock


class AsyncTest(unittest.TestCase):
    @mock.patch('url_handler.html_handler')
    def test_fetch(self, handler_mock: mock.Mock):
        url = 'https://en.wikipedia.org/wiki/Christian_Weise'
        top = 'foo'

        session_mock = mock.Mock()
        resp_mock = mock.Mock()
        handler_mock.return_value = top
        print_mock = mock.Mock()
        queue_mock = mock.AsyncMock()

        get_mock = mock.MagicMock()
        get_mock.__aenter__.return_value = resp_mock
        session_mock.get.return_value = get_mock
        resp_mock.read = mock.AsyncMock()
        resp_mock.return_value = url
        resp_mock.status = 200

        asyncio.run(fetch(session_mock, queue_mock, print_mock))

        print_mock.assert_called_once_with(f'url:{url}, top:{top}')

    @mock.patch('url_handler.html_handler')
    def test_batch_fetch(self, handler_mock: mock.Mock):
        urls = ['https://en.wikipedia.org/wiki/Christian_Weise']*10
        top = 'foo'
        handler_mock.return_value = top
