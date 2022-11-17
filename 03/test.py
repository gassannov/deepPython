import unittest
from custom_list import MyList


class DZ3Test(unittest.TestCase):
    def test_sum(self):
        my_list = MyList([1, 2, 3, 4])
        self.assertEqual(sum(my_list), 10)

    def test_sub(self):
        my_list1 = MyList([1, 2, 3])
        my_list2 = MyList([0, 1, 2])
        list1 = [0, 1, 2]
        my_list1 -= my_list2  # вычитание кастомных списков
        self.assertListEqual(list(my_list1), [1, 1, 1])
        self.assertListEqual(list(my_list2), [0, 1, 2])
        my_list2 -= list1  # вычитание с обычным списком
        self.assertListEqual(list(my_list2), [0, 0, 0])
        my_list3 = list1 - my_list2  # обычный список слева
        self.assertListEqual(list(my_list3), [0, 1, 2])
        self.assertListEqual(list(my_list2), [0, 0, 0])

    def test_sub_not_equal_len(self):
        my_list1 = MyList([1, 2, 3, 1])
        my_list2 = MyList([0, 1, 2])
        list1 = [0, 1]
        my_list1 -= my_list2  # вычитание кастомных списков разной длины
        self.assertListEqual(list(my_list1), [1, 1, 1, 1])
        self.assertListEqual(list(my_list2), [0, 1, 2])
        my_list2 -= list1  # вычитание с обычным списком разной длины
        self.assertListEqual(list(my_list2), [0, 0, 2])
        my_list3 = list1 - my_list2  # обычный список слева
        self.assertListEqual(list(my_list3), [0, 1, -2])
        self.assertListEqual(list(my_list2), [0, 0, 2])

    def test_add(self):
        my_list1 = MyList([1, 2, 3])
        my_list2 = MyList([0, 1, 2])
        list1 = [0, 1, 2]
        my_list1 += my_list2  # сложение кастомных списков
        self.assertListEqual(list(my_list1), [1, 3, 5])
        self.assertListEqual(list(my_list2), [0, 1, 2])
        my_list2 += list1  # сложение с обычным списком
        self.assertEqual(list(my_list2), [0, 2, 4])
        my_list3 = list1 + my_list2  # обычный список слева
        self.assertListEqual(list(my_list3), [0, 3, 6])

    def test_add_not_equal_len(self):
        my_list1 = MyList([1, 2, 3, 7])
        my_list2 = MyList([0, 1, 2])
        list1 = [0, 1]
        my_list1 += my_list2  # сложение кастомных списков
        self.assertListEqual(list(my_list1), [1, 3, 5, 7])
        self.assertListEqual(list(my_list2), [0, 1, 2])
        my_list2 += list1  # сложение с обычным списком разной длины
        self.assertListEqual(list(my_list2), [0, 2, 2])
        my_list3 = list1 + my_list2  # обычный список слева
        self.assertListEqual(list(my_list3), [0, 3, 2])

    def test_get_index(self):
        my_list1 = MyList([1, 2, 3])
        self.assertEqual(my_list1[1], 2)

    def test_greater(self):
        my_list1 = MyList([1, 2, 3, 7])
        my_list2 = MyList([0, 1, 2])
        self.assertGreater(my_list1, my_list2)
        self.assertNotEqual(my_list1, my_list2)
        self.assertGreaterEqual(my_list1, my_list2)

    def test_less(self):
        my_list1 = MyList([1, 2, 3, 7])
        my_list2 = MyList([0, 1, 2])
        self.assertLess(my_list2, my_list1)
        self.assertNotEqual(my_list1, my_list2)
        self.assertLessEqual(my_list2, my_list1)

    def test_equal(self):
        my_list1 = MyList([1, 2, 3, 7])
        my_list2 = MyList([0, 1, 2])
        my_list2 += [5, 5]
        self.assertEqual(my_list1, my_list2)

    def test_str(self):
        my_list1 = MyList([1, 2, 3])
        self.assertEqual(str(my_list1), '[1, 2, 3] sum is 6')