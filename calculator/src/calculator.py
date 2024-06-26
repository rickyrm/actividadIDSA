class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    def babylonian_sqrt(self, n, precision=0.001):
        if n < 0:
            raise ValueError("No se puede sacar la raiz cuadrada de un numero negativo")
        x = n
        y = (x + n / x) / 2
        while abs(x - y) > precision:
            x = y
            y = (x + n / x) / 2
        return y

    def sqrt(self, n):
        return self.babylonian_sqrt(n)







