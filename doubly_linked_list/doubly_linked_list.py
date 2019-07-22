"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length < 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

        self.length += 1

    def remove_from_head(self):
        if not self.head:
            return None
        if self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            temp = self.head
            self.head.delete
            self.head = temp.next
            return temp.value
        self.length -= 1

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            temp = self.tail
            self.tail.delete()
            self.tail = temp.prev
            return temp.value
        self.length -= 1

    def move_to_front(self, node):
        if self.length < 1:
            return None
        current = self.head
        new_node = ListNode(node)
        count = 0
        if self.length == 1:
            return current.value
        elif self.length == 2:
            temp = self.head.value
            self.head.value = self.tail.value
            self.tail.value = temp
        else:
            while current.value != new_node.value:
                if count == self.length:
                    return None
                temp = self.head.value
                self.head.value = current.next.value
                self.head.next.value = temp
                count += 1
        return self.head.value

    def move_to_end(self, node):
        if self.length < 1:
            return None
        self.tail.insert_after(node.value)
        self.tail = self.tail.next
        if node is self.head:
            self.head = self.head.next
        node.delete()

    def delete(self, node):
        # if self.length < 1:
        #     return None
        if self.length == 1 and node.value == self.head.value:
            self.head = None
            self.tail = None
        if node == self.head:
            self.head = self.head.next
        node.delete()
        self.length -= 1
        # if self.length == 1 and node.value == self.head.value:
        #     self.head = None
        #     self.tail = None
        # self.length -= 1
        # return node.delete()

    def get_max(self):
        max_value = self.head.value
        next_value = self.head.next

        while next_value:
            if next_value.value > max_value:
                max_value = next_value.value
            next_value = next_value.next
        return max_value


# my_node = ListNode(1)
# my_list = DoublyLinkedList(my_node)

# my_list.add_to_head(40)
# my_list.move_to_end(my_list.head)


# print("head: ", my_list.head.value, "Tail: ", my_list.tail.value)
# print("head prev: ", my_list.head.prev,
#       "head value : ", my_list.head.value,
#       "head next val: ", my_list.head.next.value,
#       "Tail prev val: ", my_list.tail.prev.value,
#       "Tail val: ", my_list.tail.value)
# print("head prev : ", my_list.head.prev, "Tail prev : ", my_list.tail.prev)
# print("head next : ", my_list.head.next, "Tail next: ", my_list.tail.next)
# # print("head prev : ", my_list.head.prev.value,
# #       "Tail prev : ", my_list.tail.prev.value)
# print("head next : ", my_list.head.next.value,
#       "Tail prev: ", my_list.tail.prev.value)
