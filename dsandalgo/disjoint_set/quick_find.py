class UnionFind:
    def __init__(self, size):
        self.root = [0] * size
        for i in range(0, size):
            self.root[i] = i

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(0, len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.is_connected(1, 5))  # true
print(uf.is_connected(5, 7))  # true
print(uf.is_connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.is_connected(4, 9))  # true
