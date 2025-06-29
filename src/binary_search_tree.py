class BSTNode:
    def __init__(self, val: int | None = None):
        self.left: "BSTNode| None" = None
        self.right: "BSTNode| None" = None
        self.val: int | None = val

    def insert(self, val: int):
        if self.val is None:
            self.val = val
            return
        # Do nothing when value is equal
        if self.val == val:
            return

        if self.val > val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
