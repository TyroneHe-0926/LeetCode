# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    """I just finnessed by saving it to an arr"""
    def __init__(self, iterator: Iterator):
        self.arr = []
        while iterator.hasNext(): self.arr.append(iterator.next())
        self.pointer = 0

    def peek(self) -> int:
        return self.arr[self.pointer]
        
    def next(self) -> int:
        cur = self.arr[self.pointer]
        self.pointer+=1
        return cur

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr)

class PeekingIterator:
    """Actual Iterator with saving next value, no cheese"""
    def __init__(self, iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        to_return = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return to_return

    def hasNext(self):
        return self._next is not None