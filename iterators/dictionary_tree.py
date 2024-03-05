class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Treectionary:
    def __init__(self):
        self.root = TreeNode(None)

    def __iter__(self):
        return self._traverse_tree(self.root)

    def __setitem__(self, key, value):
        node = self._find_node(self.root, key)
        if node:
            node.value = value
        else:
            self._insert_node(self.root, key, value)

    def __getitem__(self, key):
        node = self._find_node(self.root, key)
        if node:
            return node.value
        else:
            raise KeyError(f"Key '{key}' not found in the tree.")

    def __delitem__(self, key):
        self._delete_node(self.root, key)
        
    def _find_node(self, current_node, key):
        if current_node.key == key:
            return current_node
        for child in current_node.children:
            result = self._find_node(child, key)
            if result:
                return result
        return None

    def _insert_node(self, current_node, key, value):
        new_node = TreeNode(key, value)
        current_node.add_child(new_node)

    def _delete_node(self, current_node, key):
        for child in current_node.children:
            if child.key == key:
                current_node.children.remove(child)
                return
            self._delete_node(child, key)

    def _traverse_tree(self, current_node):
        if current_node.key is not None:
            yield current_node.key, current_node.value
        for child in current_node.children:
            yield from self._traverse_tree(child)
    
    def clear(self):
        self.root.children = []

    def keys(self):
        return [key for key, _ in self._traverse_tree(self.root)]

    def values(self):
        return [value for _, value in self._traverse_tree(self.root)]

    def pop(self, key, default=None):
        node = self._find_node(self.root, key)
        if node:
            value = node.value
            self._delete_node(self.root, key)
            return value
        elif default is not None:
            return default
        else:
            raise KeyError(f"Key '{key}' not found in the tree.")

    def setdefault(self, key, default=None):
        node = self._find_node(self.root, key)
        if node:
            return node.value
        else:
            self._insert_node(self.root, key, default)
            return default

