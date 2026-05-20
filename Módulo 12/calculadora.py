
class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Erro: Divisão por zero não permitida!")
        return a / b
        
      
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
    

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 3), 9)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
    

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)

if __name__ == '__main__':
    unittest.main()