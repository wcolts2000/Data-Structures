class Heap:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return str(self.storage)

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # swap first index with last index
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]

        # capture popped end of array
        removed_val = self.storage.pop()
        # sift down index 0
        self._sift_down(0)
        # return removed capture
        return removed_val

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
        # declare max index with arr length
        list_length = len(self.storage) - 1

        # shortened variable name for clarity
        arr = self.storage

        # while there is the chance of a right child
        while 2 * index + 2 <= list_length:
            left = 2 * index + 1
            right = 2 * index + 2
            # declare changing variables for while loop
            # if the left child is bigger than the right child
            if arr[left] >= arr[right]:
                # swap left with child and index
                if arr[index] <= arr[left]:
                    self.swap(index, left)
                    # set new index location to check if values there need swapping
                    index = left
            # if right is larger than left child
            elif arr[left] <= arr[right]:
                # and right is larger than index locations value
                if arr[index] <= arr[right]:
                    self.swap(index, right)
                    # swap and reassign index
                    index = right
            # otherwise break out
            else:
                return

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
