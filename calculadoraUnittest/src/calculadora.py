class CalculadoraUnittest:

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def raiz_cuadrada(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return self.aproximar_raiz_cuadrada(a)

    def exponencial(self, x):
        return self.aproximar_exponencial(x)

    def aproximar_raiz_cuadrada(self, a, precision=0.001):
        x = a
        while True:
            raiz = 0.5 * (x + a / x)
            if abs(raiz - x) < precision:
                return raiz
            x = raiz

    def aproximar_exponencial(self, x, precision=0.001):
        n = 100  # número de términos en la serie de Taylor
        e = 1
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            e += x ** i / factorial
        return e
