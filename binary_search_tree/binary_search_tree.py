class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.left and self.left.value == target or self.right and self.right.value == target:
            return True
        elif self.left is None and self.right is None:
            return False
        elif self.value > target:
            return self.left.contains(target)
        elif self.value < target:
            return self.right.contains(target)
        else:
            return False

    def get_max(self):
        while self.right is not None:
            self = self.right
        return self.value

    def for_each(self, cb):
        pass
