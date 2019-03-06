"""Built based on a solution provided in Pluralsight's Python Beyond the Basics course. Customized by me."""
from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain

# Terminal timing test
# python -m timeit -n 1 -s "from random import randrange; from sorted_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000)); [s.count(i) for i in range(1000)]"


class SortedSet(Sequence, Set):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        """
        Note to Matt: This implementation is faster than default contains because the list is sorted.
        Default contains traverses the entire list, which would be important if the list wasn't known
        to be sorted. By nature the lists in this class will always be sorted, so this is a targeted
        contains that performs more than 50% faster.
        """
        index = bisect_left(self._items, item)
        return (index != len(self._items)) and (self._items[index] == item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def _is_unique_and_sorted(self):
        return all(self[i] < self[i + 1] for i in range(len(self) - 1))

    def index(self, item, **kwargs):
        assert self._is_unique_and_sorted()
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        assert self._is_unique_and_sorted()
        return int(item in self)

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)
