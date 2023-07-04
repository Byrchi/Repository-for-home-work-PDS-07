class Node :
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Додавання нового елементу
    def insert(self, key):
        if key < self.val:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Node(key)
                return
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Node(key)
                return

# Поточні ноди в дереві
    current_node = []
    def current_nodes(self):
        self.current_node.append(self.val)
        if self.left:
            self.left.current_nodes()
        if self.right:
            self.right.current_nodes()
        return self.current_node

    def min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

####################Task_01#####################

    def add_node_in_list(self, list):
        for item in list:
            self.insert(item)

################################################

####################Task_02#####################

# Максмальне значення ноди
    def min_val_node(self):
        return min(self.current_nodes())


# Мінімальне значення ноди
    def max_val_node(self):
        return max(self.current_nodes())

################################################



####################Task_03#####################

# Видалення елементу з дерева
    def delete(self, key):
        if key < self.val:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.val:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.min_val_node()
                self.val = min_val
                self.right = self.right.delete(min_val)
        return self

################################################


