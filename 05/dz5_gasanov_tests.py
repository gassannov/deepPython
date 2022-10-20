import unittest
from dz5_gasanov_dp_LRU import LRUCache
from dz5_gasanov_dp_generator import generator_file


class LRUTest(unittest.TestCase):
    def tests(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), 'val2')
        self.assertEqual(cache.get("k1"), 'val1')
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), 'val3')
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), 'val1')
        cache.set("k2", "val2")

class GeneratorTest(unittest.TestCase):
    def tests(self):
        out_str = [str for str in generator_file(file='test.txt', words='dolor eu sunt')]
        self.assertListEqual(out_str, [
            "Lorem ipsum dolor sit amet, consectetur\n",
            "dolor in reprehenderit in voluptate velit esse cillum\n",
            "dolore eu fugiat nulla pariatur.\n",
            "proident, sunt in culpa qui officia deserunt\n"
        ])