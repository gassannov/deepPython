class MyList(list):
    def __init__(self, *args, array=None):
        if array:
            super().__init__(array)
        else:
            super().__init__(args)

    def sum(self):
        return sum(self)

    def __str__(self):
        return f'{list(self)} sum is {sum(self)}'

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            print(f'Index out of range (len is {len(self)})')
            return None

    def __add__(self, other):
        len_self = len(self)
        len_other = len(other)
        new_array = []
        for i in range(max(len_self, len_other)):
            left = self[i] if i < len_self else 0
            right = other[i] if i < len_other else 0
            new_array.append(left+right)
        return MyList(array=new_array)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        len_self = len(self)
        len_other = len(other)
        new_array = []
        for i in range(max(len_self, len_other)):
            left = self[i] if i < len_self else 0
            right = other[i] if i < len_other else 0
            new_array.append(left - right)
        return MyList(array=new_array)

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __le__(self, other):
        return self.sum() <= other.sum()

    def __ne__(self, other):
        return self.sum() != other.sum()

    def __gt__(self, other):
        return self.sum() > other.sum()

    def to_list(self):
        arr = []
        for item in self:
            arr.append(item)
        return arr
