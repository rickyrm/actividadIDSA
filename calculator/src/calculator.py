# src/calculator.py
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def babylonian_sqrt(n, precision=0.001):
        if n < 0:
            raise ValueError("Cannot take square root of a negative number")
        x = n
        y = (x + n / x) / 2
        while abs(x - y) > precision:
            x = y
            y = (x + n / x) / 2
        return y

    def sqrt(self, n):
        return self._babylonian_sqrt(n)







