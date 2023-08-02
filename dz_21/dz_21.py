class Matrix():

# Визначеня обєкуту класу матриця

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

# Перевизначаю метод __str__ для виведення на друк матриці

    def __str__(self):
        p_matrix = ""
        for row in self.data:
            p_matrix += " ".join(map(str, row)) + "\n"
        return p_matrix

# Данний метод повертає кортеж з розмірнітю матриці

    def get_shape(self):
        return len(self.data), len(self.data[0]) if self.data else (0, 0)



    def add(self, other):

        """Метод додавання матриць. Спочатку отримує розмірність додаємих матриц та визначає найбільші показники
        для приведення одної до одної в середені методу створюємо нову матрицю в яку по елементно додаємо суму
        відповідних елементів з додоємих матриць"""

        rows_self, cols_self = self.get_shape()
        rows_other, cols_other = other.get_shape()

        max_rows = max(rows_self, rows_other)
        max_cols = max(cols_self, cols_other)

        self.resize(max_rows, max_cols)
        other.resize(max_rows, max_cols)

        result = Matrix()
        for i in range(max_rows):
            row = [self.data[i][j] + other.data[i][j] for j in range(max_cols)]
            result.data.append(row)
        return result

    def multiply(self, other):

        """Метод множення  матриць. Отримуємо розмірність матриць та порівнюємо їх, в разі невідповіності правилу множення матриць викликаємо виключну ситуацію (ValueError)
        Створюємо новий об'єкт класу до якого додаємо поетапно суму добутків елементів відповідних матриць."""

        rows_self, cols_self = self.get_shape()
        rows_other, cols_other = other.get_shape()

        if cols_self != rows_other:
            raise ValueError("Matrix dimensions are not compatible for multiplication.")

        result = Matrix()
        for i in range(rows_self):
            row = []
            for j in range(cols_other):
                val = sum(self.data[i][k] * other.data[k][j] for k in range(cols_self))
                row.append(val)
            result.data.append(row)
        return result

    def multiply_by_constant(self, const):

        """Метод множення  матриці на константу . Покроково перемножуємо кожний елемент матриці на константу"""

        result = Matrix()
        for i in range(len(self.data)):
            row = [self.data[i][j] * const for j in range(len(self.data[0]))]
            result.data.append(row)
        return result

    def transpose(self):

        """Мктод транспонування . Змінює положення рядків та стовпчиків відповно"""

        rows, columns = self.get_shape()
        result = Matrix([[self.data[j][i] for j in range(rows)] for i in range(columns)])
        return result

    def resize(self, new_rows, new_cols):

        """ Метод приведеня матриць до єиного розміру. При не відповідності розмірів матриць додає елемент ( 0 ) до кожного рядка та стовпчика відповіно."""
        rows, cols = self.get_shape()
        if new_rows > rows:
            for i in range(new_rows - rows):
                self.data.append([0] * cols)
        if new_cols > cols:
            for row in self.data:
                for i in range(new_cols - cols):
                    row.append(0)


A = Matrix([[1, 2, 3], [4, 5, 6]])
B = Matrix([[9, 6], [8, 5], [7, 4]])
print(A)
print(B)
print(A.multiply(B))
print(A.multiply_by_constant(10))
print(A.add(B))
print(A.transpose())
print(A.get_shape())

