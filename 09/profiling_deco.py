from functools import wraps
from memory_profiler import profile
from io import StringIO


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != '_']


def profiling_deco(input_func):
    @wraps(input_func)
    def wrapper(*args, **kwargs):
        if 'stats' not in props(wrapper):
            wrapper.stats = StringIO()
        if 'call_num' not in props(wrapper):
            wrapper.call_num = 0
        wrapper.call_num += 1
        wrapper.stats.write(f'\n{wrapper.call_num} call of func\n')
        decorated = profile(input_func, stream=wrapper.stats)

        def print_stats():
            print(wrapper.stats.getvalue())

        wrapper.print_stats = print_stats
        return decorated(*args, **kwargs)

    return wrapper


@profiling_deco
def add(a, b):
    return a + b


if __name__ == '__main__':
    add(0, 1)
    add(1, 2)
    add(2, 3)
    add(3, 4)
    add.print_stats()
