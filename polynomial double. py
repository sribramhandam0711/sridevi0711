class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff     # Coefficient of the term
        self.exp = exp         # Exponent of the term
        self.next = None       # Pointer to next node
        self.prev = None       # Pointer to previous node
class PolynomialDLL:
    def __init__(self):
        self.head = None
def insert_term(self, coeff, exp):
    new_node = Node(coeff, exp)
    if not self.head:  # If list is empty
        self.head = new_node
        return
    # Insert at the correct position
    curr = self.head
    prev = None
    while curr and curr.exp > exp:
        prev = curr
        curr = curr.next
    if curr and curr.exp == exp:
        curr.coeff += coeff  # Add coefficients if exponent matches
    else:
        new_node.next = curr
        new_node.prev = prev
        if prev:
            prev.next = new_node
        else:
            self.head = new_node
        if curr:
            curr.prev = new_node
ef display(self):
    node = self.head
    result = ""
    while node:
        if node.coeff != 0:
            sign = "+" if result else ""
            result += f" {sign}{node.coeff}x^{node.exp}"
        node = node.next
    print(result.strip() or "0")
def add(poly1, poly2):
    result = PolynomialDLL()
    p1 = poly1.head
    p2 = poly2.head
    while p1 and p2:
        if p1.exp > p2.exp:
            result.insert_term(p1.coeff, p1.exp)
            p1 = p1.next
        elif p2.exp > p1.exp:
            result.insert_term(p2.coeff, p2.exp)
            p2 = p2.next
        else:
            result.insert_term(p1.coeff + p2.coeff, p1.exp)
            p1 = p1.next
            p2 = p2.next
    while p1:
        result.insert_term(p1.coeff, p1.exp)
        p1 = p1.next
    while p2:
        result.insert_term(p2.coeff, p2.exp)
        p2 = p2.next
    return result
