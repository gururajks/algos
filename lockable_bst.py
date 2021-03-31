import os, json
import collections


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.lockable = True
        self.locked = False
        self.parent_node = None


class LockableBST:

    def __init__(self, root):
       self.root = root

    def is_locked(self, node):
        return node.locked

    def lock(self, node):
        if not self.is_locked(node) or not node.lockable:
            return False

        node.locked = True
        while node and not node.lockable:
            node.lockable = False
            node = node.parent_node
        return True

    def unlock(self, node):
        if not self.is_locked(node) or not node.lockable:
            return False

        node.locked = False

        while node and not node.lockable and not node.locked:
            node.lockable = True
            node = node.parent_node

        return True


