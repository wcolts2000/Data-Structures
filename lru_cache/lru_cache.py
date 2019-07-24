from doubly_linked_list import DoublyLinkedList


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'key: {self.key}, value: {self.value}'

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()

    def __str__(self):
        return f'limit: {self.limit}, cache: {self.cache}'
    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache.
  """

    def get(self, key):
        if self.cache.length == 0:
            return None
        # iterate through list to find if value exists
        current = self.cache.head
        while current:
            # if it does, bubble it to the head and return its value
            val_to_return = None
            while current.next is not None:
                if current.next.value.get_key() == key:
                    val_to_return = current.next.value.get_value()
                    current = current.next
                    node_to_add = current.value
                    self.cache.delete(current)
                    self.cache.add_to_head(node_to_add)
                    break
                else:
                    current = current.next
            return val_to_return

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply
  want to overwrite the old value associated with the key with
  the newly-specified value.
  """

    def set(self, key, value):
        # print("\n NEW SET \n")
        obj = Node(key, value)
        # add to head until cache limit is reached
        if self.cache.length < self.limit:
            present = self.get(key)
            # then check if key exists in cache
            if present is not None:
                self.cache.head.value.set_value(value)
            # if it DOES exist, bubble node to head and update value
            else:
                self.cache.add_to_head(obj)

        # if it is at the limit,
        # if self.cache.length == self.limit:
        else:
            present = self.get(key)
            # then check if key exists in cache
            if present is not None:
                return self.cache.head.value.set_value(value)
            # if it DOES exist, bubble node to head and update value
            else:

                # remove from tail and add new value to head
                self.cache.remove_from_tail()
                self.cache.add_to_head(obj)


# new_cache = LRUCache(3)
# new_cache.set('item1', 'a')
# new_cache.set('item2', 'b')
# new_cache.set('item3', 'c')
# new_cache.get('item1')
# new_cache.set('item2', 'z')
# new_cache.get('item1')
# new_cache.get('item2')
# new_cache.get('item3')
# new_cache.set('item1', 'a')
# new_cache.set('item2', 'b')
# new_cache.set('item3', 'c')
# print(new_cache.get('item1'), 'a')
# new_cache.set('item4', 'd')
# print(new_cache.get('item1'), 'a')
# print(new_cache.get('item3'), 'c')
# print(new_cache.get('item4'), 'd')
# print(new_cache.get('item2'), None)
