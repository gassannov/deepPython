class MyList(list):

    def __str__(self):
        return f'{list(self)} sum is {sum(self)}'

    def __add__(self, other):
        len_self = len(self)
        len_other = len(other)
        new_array = []
        for i in range(max(len_self, len_other)):
            left = self[i] if i < len_self else 0
            right = other[i] if i < len_other else 0
            new_array.append(left+right)
        return MyList(new_array)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return MyList.__sub__(other, self)

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
        return MyList(new_array)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
