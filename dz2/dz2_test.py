import unittest
from unittest.mock import patch
import dz2
import factory


class TestJSON(unittest.TestCase):
    json_str = '{"word1": "foo bar", "word2": "some bar","word3": "some foo","word4": "some loren ' \
               'ipsum","word5": "dolor sit","word6": "python code"}'

    @patch("dz2.callback_func")
    def test_simple(self, callback_mock):
        json_str_error = "some_str"
        dz2.parse_json(json_str_error, callback_mock)
        self.assertFalse(callback_mock.called)

    @patch("dz2.callback_func")
    def test_none_fields(self, callback_mock):
        dz2.parse_json(TestJSON.json_str, callback_mock)
        self.assertFalse(callback_mock.called)

    @patch("dz2.callback_func")
    def test_none_keywords(self, callback_mock):
        dz2.parse_json(TestJSON.json_str, callback_mock, required_fields=['word1'])
        self.assertFalse(callback_mock.called)

    @patch("dz2.callback_func")
    def test_one_call(self, callback_mock):
        dz2.parse_json(TestJSON.json_str, callback_mock, required_fields=['word1'], keywords=['bar'])
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)

    @patch("dz2.callback_func")
    def test_two_fields(self, callback_mock):
        dz2.parse_json(TestJSON.json_str, callback_mock, required_fields=['word1', 'word2'], keywords=['bar'])
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)

    def test_type_error(self):
        result = dz2.parse_json(5)
        self.assertEqual(None, result)

    @patch("dz2.callback_func")
    def test_three_fields(self, callback_mock):
        dz2.parse_json(TestJSON.json_str, callback_mock, required_fields=['word2', 'word3', 'word4'], keywords=['some'])
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 3)
