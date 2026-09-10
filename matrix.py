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
            return new_matrix
        elif isinstance(other, Matrix):
            if self._cols == other._rows:
                new_matrix = []
                for i in range(self._rows):
                    row = []
                    for j in range(other._cols):
                        row.append(sum(self.matrix[i][q] * other.matrix[q][j] for q in range(self._cols)))
                    new_matrix.append(row)
                return new_matrix
            raise NotImplementedError
        raise TypeError

    def transposition(self):
        t = [[None for _ in range(self._rows)] for _ in range(self._cols)]
        for i in range(self._rows):
            for j in range(self._cols):
                t[j][i] = self.matrix[i][j]
        return t
