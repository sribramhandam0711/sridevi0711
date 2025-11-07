class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, coeff, power):
        new_node = Node(coeff, power)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse(self):
        terms = []
        temp = self.head
        while temp:
            terms.append(f"{temp.coeff}x^{temp.power}")
            temp = temp.next
        return " + ".join(terms) if terms else "0"

def add_polynomials(poly1, poly2):
    p1 = poly1.head
    p2 = poly2.head
    result = DoublyLinkedList()
    while p1 and p2:
        if p1.power == p2.power:
            summed = p1.coeff + p2.coeff
            if summed != 0:
                result.append(summed, p1.power)
            p1 = p1.next
            p2 = p2.next
        elif p1.power > p2.power:
            result.append(p1.coeff, p1.power)
            p1 = p1.next
        else:
            result.append(p2.coeff, p2.power)
            p2 = p2.next
    # Add remaining terms
    while p1:
        result.append(p1.coeff, p1.power)
        p1 = p1.next
    while p2:
        result.append(p2.coeff, p2.power)
        p2 = p2.next
    return result

# Example usage:
if __name__ == "__main__":
    # Polynomial 1: 5x^3 + 4x^2 + 2x^0
    poly1 = DoublyLinkedList()
    poly1.append(5, 3)
    poly1.append(4, 2)
    poly1.append(2, 0)
    # Polynomial 2: 5x^2 + 5x^1 + 5x^0
    poly2 = DoublyLinkedList()
    poly2.append(5, 2)
    poly2.append(5, 1)
    poly2.append(5, 0)
    result = add_polynomials(poly1, poly2)
    print("Result:", result.traverse())

  
    
       
