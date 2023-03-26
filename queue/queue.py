class Queue:  # FIFO
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # Utilizing a singly-linked list

    def enqueue(self, item):
        new_node = Node(item)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        temp = self.first
        self.first = self.first.next
        self.size -= 1
        return temp.value

    def len(self):
        return self.size


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
