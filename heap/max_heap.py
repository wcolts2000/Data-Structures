class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # def _bubble_up(self, index):
    #   pass
    def _bubble_up(self, index):
        while index > 0:
            # grab parents position (subtract one from index and divide by 2, floored)
            parent = (index - 1) // 2

            # compare to parent
            # if the child node is larger, swap with parent
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # change the index to the parent position and go to next iteration
                index = parent
            # once parent is no longer smaller, break the loop
            else:
                break

    def _sift_down(self, index):
        pass


'''
- Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
  - `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  - `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed.
  - `get_max` returns the maximum value in the heap _in constant time_.
  - `get_size` returns the number of elements stored in the heap.
  - `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  - `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
'''
# heap = Heap()

# heap.insert(6)
# heap.insert(8)
# heap.insert(10)
# heap.insert(9)
# heap.insert(1)
# heap.insert(9)
# heap.insert(9)
# heap.insert(5)
# print(heap.storage, [10, 9, 9, 6, 1, 8, 9, 5])
