class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):

        if isinstance(self.a, str) or isinstance(self.b, str) and isinstance(self.c, str):
            return "Vvedeny ne chisla"
        elif self.a <= 0 or self.b == 0 and self.c <= 0:
            return 'Вы не можете писать отрицательные числа!!'
        elif self.a and self.b <= self.c or self.b and self.c <= self.a or self.a and self.c <= self.b:
            return 'Треугольник не выйдет'
        else:
            return 'Ура, можно построить треугольник!'


triangle_result = TriangleChecker(2, 2, 3)
print(triangle_result.is_triangle())
