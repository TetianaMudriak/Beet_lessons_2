import itertools


def with_index(iterable, start=0):
    result = list(zip(itertools.count(start=start), iterable))
    print(result)


class RangeCreating:
    def __init__(self, _start, _end, step=1):
        self.start = _start
        self.end = _end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        val = self.start
        self.start += self.step
        return val


def in_range(iterable: RangeCreating):
    list_ = []
    for i in iterable:
        list_.append(i)
    print(list_)


class Iterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._iterable):
            self._index += 1
            return self._iterable[self._index]
        raise StopIteration


class Iterable:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return Iterator(self._data)

    def __getitem__(self, item):
        return self._data[item]


def main():
    # Task 1
    with_index(['a', 'b', 'c'])

    # Task 2
    # range1 = RangeCreating(1, 5)
    in_range(RangeCreating(1, 8, 2))

    # Task 3
    list1 = [1, 2, 3]
    print(len(list1))
    iter1 = Iterable(list1)
    print(iter1[0])


if __name__ == '__main__':
    main()
