from fraction import Fraction


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self._rows = len(matrix)
        self._cols = len(matrix[0])

    def __add__(self, other):
        if self._rows == len(other.matrix) and self._cols == len(other.matrix[0]):
            new_matrix = []
            for i in range(self._rows):
                row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self._cols)]
                new_matrix.append(row)
            return new_matrix
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_matrix = []
            for i in range(self._rows):
                row = [self.matrix[i][j] * other for j in range(self._cols)]
                new_matrix.append(row)
            return Matrix(new_matrix)
        elif isinstance(other, Matrix):
            if self._cols == other._rows:
                new_matrix = []
                for i in range(self._rows):
                    row = []
                    for j in range(other._cols):
                        row.append(sum(self.matrix[i][q] * other.matrix[q][j] for q in range(self._cols)))
                    new_matrix.append(row)
                return Matrix(new_matrix)
            raise NotImplementedError
        raise TypeError


    @staticmethod
    def zero_matrix(n, m):
        return Matrix([[0 for _ in range(m)] for _ in range(n)])

    @staticmethod
    def identity_matrix(n):
        return Matrix([[1 if i == j else 0 for i in range(n)] for j in range(n)])

    @staticmethod
    def _minor(a, i, j):
        return [a[i1][0:j] + a[i1][j + 1:] for i1 in range(len(a)) if i1 != i]

    def transposition(self):
        t = Matrix([[None for _ in range(self._rows)] for _ in range(self._cols)])
        for i in range(self._rows):
            for j in range(self._cols):
                t[j][i] = self.matrix[i][j]
        return t

    @staticmethod
    def _det(a):
        if len(a) == 1:
            return a[0][0]
        res = 0
        for j in range(len(a)):
            res += a[0][j] * (-1) ** j * Matrix._det(Matrix._minor(a, 0, j))
        return res

    def determinant(self):
        if self.is_square():
            return Matrix._det(self.matrix)
        raise NotImplementedError("Determinant is defined only for square matrices")

    def __getitem__(self, item):
        return self.matrix[item]

    def is_square(self):
        return self._rows == self._cols

    def inverse(self):
        n = self._cols
        det = Matrix._det(self.matrix)
        if det == 0:
            raise ZeroDivisionError
        adj = Matrix([[[] for _ in range(n)] for _ in range(n)])
        for i in range(n):
            for j in range(n):
                adj[i][j] = Matrix._det(self._minor(self.matrix, i, j)) * (-1) ** (i + j)
        return adj.transposition() * (1 / det)

    def show(self):
        for row in self.matrix:
            #print(row)
            print(list(map(lambda r: round(r, 3), row)))

    def __repr__(self):
        return f"Matrix(matrix={self.matrix!r})"


m = Matrix([
    [1, 2, 3],
    [4, -5, 6],
    [7, 8, 9]
])
m.inverse().show()