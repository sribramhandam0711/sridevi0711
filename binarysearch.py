class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)
          bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:")
bst.inorder()

result = bst.search(40)
if result:
    print("Found:", result.data)
else:
    print("Not Found")

