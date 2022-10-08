import unittest
from dz3_gasanov_dp import MyList


class DZ3Test(unittest.TestCase):
    def test_sum(self):
        my_list = MyList(1, 2, 3, 4)
        self.assertEqual(my_list.sum(), 10)

    def test_sub(self):
        my_list1 = MyList(1, 2, 3)
        my_list2 = MyList(0, 1, 2)
        my_list1 -= my_list2
        self.assertListEqual(my_list1.to_list(), [1, 1, 1])

    def test_sub_not_equal_len(self):
        my_list1 = MyList(1, 2, 3, 1)
        my_list2 = MyList(0, 1, 2)
        my_list1 -= my_list2
        self.assertListEqual(my_list1.to_list(), [1, 1, 1, 1])
        self.assertListEqual(my_list2.to_list(), [0, 1, 2])

    def test_add(self):
        my_list1 = MyList(1, 2, 3)
        my_list2 = MyList(0, 1, 2)
        my_list3 = my_list1 + my_list2
        self.assertListEqual(my_list3.to_list(), [1, 3, 5])

    def test_add_not_equal_len(self):
        my_list1 = MyList(1, 2, 3, 7)
        my_list2 = MyList(0, 1, 2)
        my_list3 = my_list1 + my_list2
        self.assertListEqual(my_list1.to_list(), [1, 2, 3, 7])
        self.assertListEqual(my_list2.to_list(), [0, 1, 2])
        self.assertListEqual(my_list3.to_list(), [1, 3, 5, 7])

    def test_get_index(self):
        my_list1 = MyList(1, 2, 3)
        self.assertEqual(my_list1[1], 2)

    def test_greater(self):
        my_list1 = MyList(1, 2, 3, 7)
        my_list2 = MyList(0, 1, 2)
        self.assertGreater(my_list1, my_list2)
        self.assertNotEqual(my_list1, my_list2)
        self.assertGreaterEqual(my_list1, my_list2)

    def test_equal(self):
        my_list1 = MyList(1, 2, 3, 7)
        my_list2 = MyList(0, 1, 2)
        my_list2 += [5, 5]
        self.assertEqual(my_list1, my_list2)

    def test_str(self):
        my_list1 = MyList(1, 2, 3)
        self.assertEqual(str(my_list1), '[1, 2, 3] sum is 6')