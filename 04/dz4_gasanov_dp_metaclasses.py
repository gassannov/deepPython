class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        custom_attr = {}
        for name_, value in dct.items():
            if not name_.startswith('__') and not name_.endswith('__'):
                custom_attr[f'custom_{name_}'] = value
                continue
            custom_attr[name_] = value
        return super().__new__(cls, name, bases, custom_attr)

    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        return inst

    def __setattr__(cls, key, value):
        if not key.startswith('custom'):
            key = f'custom_{key}'
        super(CustomMeta, cls).__setattr__(key, value)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

    def __setattr__(self, key, value):
        super().__setattr__(f'custom_{key}', value)
