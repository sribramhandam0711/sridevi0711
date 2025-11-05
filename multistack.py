class kStacks:

    # main array to store elements
    def __init__(self, n, k):
        self.segSize = n // k
        self.arr = [0] * n
        self.top = [i * self.segSize - 1 for i in range(k)]

    # push element x into stack i
    def push(self, x, i):
        end = (i + 1) * self.segSize - 1

        if self.top[i] == end:
            print(f'Stack {i} overflow')
            return

        self.top[i] += 1
        self.arr[self.top[i]] = x

    # pop element from stack i
    def pop(self, i):
        start = i * self.segSize

        if self.top[i] < start:
            print(f'Stack {i} underflow')
            return -1

        val = self.arr[self.top[i]]
        self.top[i] -= 1
        return val


if __name__ == '__main__':
    n = 4
    k = 2
    st = kStacks(n, k)

    # Each operation has the following format:
    # 1. Push operation → [1, value, stackNumber]
    # 2. Pop operation  → [2, stackNumber]
    operations = [
        [1, 5, 0],
        [1, 9, 0],
        [1, 10, 0],
        [1, 15, 1],
        [2, 0],
        [2, 1],
        [2, 1]
    ]
    
    for op in operations:
        if op[0] == 1:
            x = op[1]
            m = op[2]
            st.push(x, m)
        elif op[0] == 2:
            m = op[1]
            res = st.pop(m)
            if res != -1:
                print(f'Popped Element: {res}')
