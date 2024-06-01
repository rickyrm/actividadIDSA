import unittest
from calculator import CalculadoraUnittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraUnittest()

    def test_suma(self):
        self.assertEqual(self.calc.suma(1, 2), 3)
        self.assertEqual(self.calc.suma(-1, 1), 0)
        self.assertEqual(self.calc.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(self.calc.resta(3, 2), 1)
        self.assertEqual(self.calc.resta(-1, 1), -2)
        self.assertEqual(self.calc.resta(-1, -1), 0)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(2, 3), 6)
        self.assertEqual(self.calc.multiplicacion(-1, 1), -1)
        self.assertEqual(self.calc.multiplicacion(-1, -1), 1)

    def test_division(self):
        self.assertEqual(self.calc.division(6, 3), 2)
        self.assertEqual(self.calc.division(-1, 1), -1)
        self.assertEqual(self.calc.division(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calc.division(1, 0)

    def test_raiz_cuadrada(self):
        self.assertAlmostEqual(self.calc.raiz_cuadrada(4), 2, places=3)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(9), 3, places=3)
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-1)

    def test_exponencial(self):
        self.assertAlmostEqual(self.calc.exponencial(1), 2.718, places=3)
        self.assertAlmostEqual(self.calc.exponencial(0), 1, places=3)

if __name__ == '__main__':
    unittest.main()
