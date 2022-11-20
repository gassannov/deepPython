import time
import weakref
from memory_profiler import profile
from threading import Thread


class SomeClass:
    def __init__(self, name):
        self.name = name


class SlotsAttrs:
    __slots__ = ('name1', 'name2')

    def __init__(self):
        self.name1 = SomeClass('name')
        self.name2 = SomeClass('surname')


class SimpleAttrs:
    def __init__(self):
        self.name1 = SomeClass('name1')
        self.name2 = SomeClass('name2')


class WeakRefAttrs:
    def __init__(self):
        self.name1 = weakref.ref(SomeClass('name1'))
        self.name2 = weakref.ref(SomeClass('name2'))


def attr_speed_test(cls_list):
    start = time.time()
    for cls in cls_list:
        b = cls.name1
        b = cls.name2
        cls.name1 = SomeClass('new')
        cls.name2 = SomeClass('new')
        del cls.name1
        del cls.name2
    end = time.time()
    return end - start


@profile
def run_tests(repeat_cnt, is_print=True):
    start = time.time()
    list_slots = [SlotsAttrs() for _ in range(repeat_cnt)]
    end = time.time()
    slots_time = end-start

    start = time.time()
    list_weakref = [WeakRefAttrs() for _ in range(repeat_cnt)]
    end = time.time()
    weakref_time = end - start

    start = time.time()
    list_simple = [SimpleAttrs() for _ in range(repeat_cnt)]
    end = time.time()
    simple_time = end - start

    time_attrs_slots = attr_speed_test(list_slots)
    time_attrs_weakref = attr_speed_test(list_weakref)
    time_attrs_simple = attr_speed_test(list_simple)
    if is_print:
        print(f'slots init time: {slots_time}\nslots attrs access time: {time_attrs_slots}\n')
        print(f'weakref init time: {weakref_time}\nweakref attrs access time: {time_attrs_weakref}\n')
        print(f'simple init time: {simple_time}\nsimple attrs access time: {time_attrs_simple}\n')


if __name__ == '__main__':
    REPEAT_CNT_PROFILER = 100_000
    run_tests(REPEAT_CNT_PROFILER)
    print(run_tests.__dict__)
