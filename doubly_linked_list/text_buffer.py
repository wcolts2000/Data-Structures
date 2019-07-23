from doubly_linked_list import DoublyLinkedList


class TextBuffer:
    # init gives us the option to initialize some text in the
    # buffer right off the bat
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            self.contents.add_to_tail(init)

    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        # print("CONTENTS: ", self.contents.head.value,
        #       "STRING TO ADD: ", string_to_add)
        self.contents.add_to_tail(string_to_add)

    def prepend(self, string_to_add):
        # reverse the incoming string to maintain correct
        # order when adding to the front of the text buffer
        self.contents.add_to_head(string_to_add)

    def delete_front(self, chars_to_remove):
        while chars_to_remove > 0:
            if len(self.contents.head.value) > chars_to_remove:
                self.contents.head.value = self.contents.tail.value[1:]
                chars_to_remove -= 1
            else:
                first_set_to_remove = len(self.contents.head.value)
                self.contents.remove_from_head()
                return self.delete_back(chars_to_remove - first_set_to_remove)

    def delete_back(self, chars_to_remove):
        while chars_to_remove > 0:
            if len(self.contents.tail.value) > chars_to_remove:
                self.contents.tail.value = self.contents.tail.value[:-1]
                chars_to_remove -= 1
            else:
                first_set_to_remove = len(self.contents.tail.value)
                self.contents.remove_from_tail()
                return self.delete_back(chars_to_remove - first_set_to_remove)

    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer 
    The tail of the concatenated buffer will be the tail of the other buffer 
    The head of the concatenated buffer will be the head of this buffer 
    """

    def join(self, other_buffer):
        # we might want to check that other_buffer is indeed a text buffer
        # print(isinstance(other_buffer, TextBuffer), "PRINTED")
        if isinstance(other_buffer, TextBuffer):
            # old_tail = self.contents.tail
            s = ""
            current = other_buffer.contents.head
            while current:
                s += current.value
                current = current.next
            # return s
            self.contents.add_to_tail(s)
            # other_buffer.contents.head.prev = old_tail

        # set self list tail's next node to be the head of the other buffer

        # set other_buffer head's prev node to be the tail of this buffer
        else:
            self.join_string(other_buffer)
            # self.join(new_buffer)
    # if we get fed a string instead of a text buffer instance,
    # initialize a new text buffer with this string and then
    # call the join method

    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        # while len(string_to_join) > 0:
        #     new_buffer.add_to_tail(string_to_join[0])
        #     print("STRING TO JOIN: ", string_to_join)
        #     string_to_join = string_to_join[1:]
        # for char in string_to_join:
        # new_buffer.contents.add_to_tail(char)
        # new_buffer.contents.add_to_tail(char)
        self.join(new_buffer)


if __name__ == '__main__':
    text = TextBuffer("Super")
    print(text)

    text.join_string("califragilisticexpealidocious")
    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(4)
    print(text)
