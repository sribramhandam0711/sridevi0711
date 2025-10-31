import math

class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0

    def add_at_end(self, t):
        self.child.append(t)
        self.order += 1

class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert_node(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if self.least is None or value < self.least.value:
            self.least = new_tree
        self.count += 1

    def get_min(self):
        return None if self.least is None else self.least.value

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            self.least = None if not self.trees else self.trees[0]
            self.consolidate()
            self.count -= 1
            return smallest.value

    def consolidate(self):
        aux = (self.count+1) * [None]
        while self.trees:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order]:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            aux[order] = x
        self.least = None
        for k in aux:
            if k:
                self.trees.append(k)
                if self.least is None or k.value < self.least.value:
                    self.least = k
