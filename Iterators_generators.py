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


def main():
    # Task 1
    with_index(['a', 'b', 'c'])

    # Task 2
    # range1 = RangeCreating(1, 5)
    in_range(RangeCreating(1, 6))


if __name__ == '__main__':
    main()