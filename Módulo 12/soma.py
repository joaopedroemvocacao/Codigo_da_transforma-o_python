
def soma(a, b):
    return a + b
  

import unittest
from somar import soma

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)
    
    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -4), -5)
    
    def test_soma_zero(self):
        self.assertEqual(soma(0, 5), 5)

if __name__ == '__main__':
    unittest.main()