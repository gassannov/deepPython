import unittest
from dz4_gasanov_dp_metaclasses import CustomMeta, CustomClass
from dz4_gasanov_dp_descriptor import Data


class TestMetaClasses(unittest.TestCase):
    def test_instance(self):
        inst = CustomClass()
        self.assertTrue(inst.custom_x == 50)
        self.assertTrue(inst.custom_val == 99)
        self.assertTrue(inst.custom_line() == 100)
        self.assertTrue(str(inst) == "Custom_by_metaclass")

    def test_class(self):
        self.assertTrue(CustomClass.custom_x == 50)

    def test_dynamic(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        t = 0
        CustomClass.foo = 1
        self.assertTrue(inst.custom_dynamic == "added later")
        self.assertEqual(CustomClass.custom_foo, 1)
        try:
            self.assertRaises(AttributeError, inst.dynamic)
        except AttributeError:
            t = 1
        self.assertTrue(t, 1)


    def test_errors(self):
        inst = CustomClass()
        inst_x = lambda : inst.x
        inst_val = lambda: inst.val
        inst_line = lambda: inst.line()
        inst_yyy = lambda: inst.yyy
        inst_class_x = lambda: CustomClass.x
        self.assertRaises(AttributeError, inst_x)
        self.assertRaises(AttributeError, inst_val)
        self.assertRaises(AttributeError, inst_line)
        self.assertRaises(AttributeError, inst_yyy)
        self.assertRaises(AttributeError, inst_class_x)


class TestDescriptor(unittest.TestCase):
    def test_num(self):
        data_right = Data(100)
        self.assertEqual(data_right.num, 100)
        a = 0
        try:
            self.assertRaises(TypeError, Data('100'))
        except TypeError:
            a = 1
        self.assertEqual(a, 1)

    def test_name(self):
        data_right = Data(name='man')
        self.assertEqual(data_right.name, 'man')
        a = 0
        try:
            self.assertRaises(TypeError, Data(name=100))
        except TypeError:
            a = 1
        self.assertEqual(a, 1)

    def test_price(self):
        data_right = Data(price=100)
        self.assertEqual(data_right.price, 100)
        a = 0
        try:
            self.assertRaises(TypeError, Data(price='100'))
            self.assertRaises(TypeError, Data(price=-100))
        except TypeError:
            a = 1
        self.assertEqual(a, 1)