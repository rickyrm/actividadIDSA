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







